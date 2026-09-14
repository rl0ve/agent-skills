// Real HID pointer events for screen capture of a native app.
//
// Accessibility clicks (AppleScript `click at`, AXPress) are accepted by an app's
// own chrome but are ignored by embedded web content, and they never move the OS
// cursor, so nothing appears in the recording. These CGEvents do both.
//
//   swiftc -O -o hid-pointer hid-pointer.swift
//   ./hid-pointer where
//   ./hid-pointer move  X Y [steps] [ms]
//   ./hid-pointer click X Y [steps] [ms]
//   ./hid-pointer scroll X Y TICKS
//
// Coordinates are global points with the origin at the top left of the main
// display. On a 1x display they equal the pixels in a `screencapture` still; on a
// Retina display they are half. Read the geometry rather than assuming, and check
// `system_profiler SPDisplaysDataType` for mirroring before trusting a capture's
// dimensions. Requires Accessibility permission for the running terminal.

import Foundation
import CoreGraphics

func post(_ event: CGEvent?) { event?.post(tap: .cghidEventTap) }

func move(_ p: CGPoint) {
    post(CGEvent(mouseEventSource: nil, mouseType: .mouseMoved,
                 mouseCursorPosition: p, mouseButton: .left))
}

/// Ease in and out so the path reads as a hand, not a jump cut.
func glide(from a: CGPoint, to b: CGPoint, steps: Int, totalMs: Double) {
    let dt = UInt32((totalMs / Double(steps)) * 1000)
    for i in 1...steps {
        let t = Double(i) / Double(steps)
        let e = t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t
        move(CGPoint(x: a.x + (b.x - a.x) * e, y: a.y + (b.y - a.y) * e))
        usleep(dt)
    }
}

func click(_ p: CGPoint) {
    move(p); usleep(120_000)
    post(CGEvent(mouseEventSource: nil, mouseType: .leftMouseDown,
                 mouseCursorPosition: p, mouseButton: .left))
    usleep(90_000)
    post(CGEvent(mouseEventSource: nil, mouseType: .leftMouseUp,
                 mouseCursorPosition: p, mouseButton: .left))
}

func scroll(_ p: CGPoint, _ ticks: Int32) {
    move(p); usleep(60_000)
    for _ in 0..<abs(Int(ticks)) {
        post(CGEvent(scrollWheelEvent2Source: nil, units: .line, wheelCount: 1,
                     wheel1: ticks > 0 ? 3 : -3, wheel2: 0, wheel3: 0))
        usleep(45_000)
    }
}

let args = CommandLine.arguments
guard args.count >= 2 else { print("need a command"); exit(1) }
let cursor = CGEvent(source: nil)?.location ?? .zero

switch args[1] {
case "where":
    print("\(cursor.x),\(cursor.y)")
case "move":
    glide(from: cursor, to: CGPoint(x: Double(args[2])!, y: Double(args[3])!),
          steps: args.count > 4 ? Int(args[4])! : 40,
          totalMs: args.count > 5 ? Double(args[5])! : 600)
case "click":
    let target = CGPoint(x: Double(args[2])!, y: Double(args[3])!)
    glide(from: cursor, to: target,
          steps: args.count > 4 ? Int(args[4])! : 40,
          totalMs: args.count > 5 ? Double(args[5])! : 600)
    click(target)
case "scroll":
    scroll(CGPoint(x: Double(args[2])!, y: Double(args[3])!), Int32(args[4])!)
default:
    print("unknown command"); exit(1)
}
