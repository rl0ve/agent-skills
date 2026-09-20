# Meaningful interaction in scenes and simulations

Use when a game, training environment, configurator or simulation asks people to
identify, manipulate or act on objects. This supplements the selected implementation
specialist. A decorative scene or static page does not need these task contracts.

## Make the visible object match the task

Keep a small mapping between each task-relevant object, its stable identity, visible
meaning, permitted actions and resulting state. A label should describe the asset
actually present. Distinguish a container from its contents, a category from a specific
instance, and different meanings of the same word. Accept equivalent instances when
the instruction permits them; require the named instance when it does not. Do not
substitute an attractive asset that changes what the instruction means.

For a relational action, validate the object, destination, relationship and relevant
state together. Selecting the right destination is insufficient if the object or
relationship is wrong. Apply the state change only after validation; an unsuccessful
attempt should leave a recoverable scene. Keep this logic separate from the input
adapter so keyboard, touch and any later controller route can express the same intent.
Shared intent does not establish that an untested input device works.

## Inspect assets at interaction distance

An imported model can contain alternate variants, detached lids, display stands or
hidden geometry. Choose the intended parts before deriving interaction bounds,
collision shapes or placement anchors. Use explicit anchors when a mesh bounding box
does not describe a usable interior or resting surface. Inspect scale, orientation and
normals with the actual task; a package thumbnail cannot establish that a carried
object fits inside a container or rests on a table.

Verify one relevant sequence through its settled result: select, carry or change,
place, cancel/reset and resume when supported. Check direct geometry selection as
well as alternate controls. Wait for the application's transition to finish before
judging placement; an intermediate animation frame can look like an incorrect result.
Recheck affected relations when an asset changes even if its stable ID is preserved.

## Keep support and evidence honest

For training or assessment, decide what a successful action demonstrates. Keep
exposure, labels/hints, assisted completion and unassisted performance distinguishable
when they affect the product's claims. A compound instruction does not independently
prove mastery of every component. Separate modalities or contexts only when those
distinctions matter to the requested outcome; do not impose a learning system on an
ordinary game or configurator.

Maintain the useful difference between catalog size and authored interactive coverage.
More entries or decorative objects do not establish more tested experiences. A design
rubric can guide implementation, but its score is not a measured completion rate,
retention result or guarantee of behavior change. Report actual user evidence separately.

Apply [motion-quality.md](motion-quality.md) for shared input ownership and asynchronous
media completion. These checks complement visual fidelity; neither substitutes for it.
