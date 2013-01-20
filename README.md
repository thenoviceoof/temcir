temcir
================================================================================

An auto-scheduling project

This was borne out of a frustration with failing to get interesting
things done, and instead have my time be sucked into a swirling vortex
of video games and the internet (among other things). As such, temcir
had to do a few things:

 - Propose variety

   Some people take the approach of a strict stack based approach to
   TODOs. That might be effective, but I am struck with inspiration
   too often to stick to that sort of plan. Hence, introducing a
   variety of near/far, or effective/fun, or long/short, or tasks from
   different fields is something temcir should be able to do.

 - Be flexible

   Trying to plan out tasks at the beginning of the day/<insert time
   interval> tends to break quickly (not survive contact) because once
   changes start rolling (ie. stop doing something because I opened
   reddit, or a task takes longer than expected) I tend to just ignore
   the rest of the planned out calendar.

 - Provide a path to 10k hours

   I want to become proficient in a number of things, but since I tend
   to do things in a bursty manner, I tend to not make progress on any
   of those things.

 - Keep me sane

   All work and no play makes jack a dull boy: maybe intentionally
   creating down time, in addition to routing around it, could be
   effective. Also, I tend to binge on stories and byte incrementing
   simulators: temcir should break up those dead zones and use them
   productively as dribbling fun.

 - Externalize my desire to get things done

   I once tossed around the idea of trying and getting my friends to
   keep me on task, but there is no bigger critic than myself, so
   relying on future selves may work out better.

 - Bi-directional quantified self

   temcir will generate info on what I actually do, vs. what I plan to
   do. Also, temcir could eventually accept, say, biometrics so fun
   gets allocated when I'm tired.

 - Interaction must be easy

   Ex. I don't use pensievr that much because it's a pain to login.
   For the other sort of interaction (API), it would be nice to be
   able to pull project ideas from the task list for a public
   interface, such that I just have an idea list I don't have to
   constantly curate.


Plan
--------------------------------------------------------------------------------

A high level plan to make this happen:

Minimum Viable Project:

 - Make a simple webapp that accepts tasks (heirarchy, tag)

 - Run a cron job that texts (twilio) you whenever temcir wants to
   propose you take up a new task, or to check that you're still
   doing the task, which leads to a link (bit.ly?)

 - The bit.ly link leads to a task selection: have one or more
   options, always with the option to take time off instead
   (difference being you're committing to a time frame, which may or
   may not have an effect), or choose from the 'backlog'. Choosing
   to run a collection of errands within a tag should also be a
   thing.

 - Have simple recurring tasks that take the place of a task after a
   certain time, which have the same extension/other
   interface. (sleeping, for example)

 - Proposition algorithm:

   - Randomly choose from the task list, weighed by priority and how
     often I've been doing the sort of task lately (by tag).

 - Schedule regular task review sessions, with the depth of sorting
   inverse to the session's regularity.
