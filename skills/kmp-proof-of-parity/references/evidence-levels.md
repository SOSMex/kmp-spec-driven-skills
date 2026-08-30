# Evidence levels

Assign evidence independently for each target and behavior. These levels describe different facts; they are not automatically cumulative across platforms.

## Compiled

The relevant source set or target compiled successfully at a named revision. Record the actual task or CI job. This does not prove tests or runtime behavior.

## Automated-tested

Relevant automated tests passed in a named environment. Describe the behavior covered and notable gaps. A JVM-hosted common test does not become native runtime evidence.

## Emulator-tested

The acceptance path was observed on an Android emulator or Apple simulator. Record the virtual device, OS version, build, steps, and artifacts. Device-sensitive behavior may remain open.

## Physically-tested

The acceptance path was observed on the required real hardware. Record device class, OS version, build, participants or device topology without private identities, and evidence. A one-device check cannot close a two-device gate.

## Store-submitted

The identified build was submitted to a named store review process. Record version/build identity and dated submission evidence. This does not mean reviewers accepted it or users can install it publicly.

## Released

The identified version is publicly available through the named distribution channel and independently verified. Record the public listing or distribution evidence and date.

## Reporting partial parity

Prefer statements such as:

> Shared rules are automated-tested on the JVM; Android is emulator-tested; iOS compiles, but its runtime flow and the physical Android-iPhone scenario remain open.

Avoid statements such as:

> The feature is fully cross-platform.

unless every acceptance criterion has the required evidence on every supported target and device combination.
