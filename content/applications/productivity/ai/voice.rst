=======================================
Voice: dictation and call transcription
=======================================

The module AI Voice adds speech to text to eYssen. You can dictate messages
instead of typing them, and you can have a Discuss call transcribed and
summarised, with action items. It uses a speech-to-text model that an
administrator configures once.

Set up speech to text
=====================

1. Add a provider that offers the OpenAI-compatible transcription route, for
   example OpenAI, or Groq or a self-hosted Whisper server using the provider
   type OpenAI with its own base URL (see :doc:`models_and_providers`).
   Anthropic and OpenRouter have no transcription route and cannot be used for
   speech to text.
2. Refresh the models of the provider. Ids that contain ``whisper`` or
   ``transcribe`` are classified as :guilabel:`Speech to text` models
   automatically.
3. Open :menuselection:`AI --> Configuration --> Settings`, find the block
   :guilabel:`Voice` and choose the :guilabel:`Speech-to-text model`. Dictation
   and call transcription stay hidden until a model is chosen.

The other settings of the block are:

- :guilabel:`Spoken language`: an optional two-letter language code such as
  ``hu`` or ``es``. Leave it empty to detect the language automatically.
- :guilabel:`Max recording size (MB)`: the limit per uploaded recording or call
  piece (10 MB by default, never more than 25 MB).
- :guilabel:`Max dictation length (seconds)`: a dictation stops by itself after
  this time (120 seconds by default).
- :guilabel:`Call chunk length (seconds)`: call audio is uploaded and
  transcribed in pieces of this length (30 seconds by default).
- :guilabel:`Max transcribed minutes per call and person` (180 by default).
- :guilabel:`Keep call audio (days)`: how long the call recordings are kept (7
  days by default). With 0 the audio is not stored at all, only the text. The
  text always stays.
- :guilabel:`Summarize calls automatically`: when a transcribed call ends, a
  summary with action items is posted in the channel (on by default).

.. note::
   Speech to text uses the AI capability Ask, the same rate limits as other AI
   requests and the daily call and cost caps. Each request is written to the AI
   log, with its cost estimated from the audio length or the token usage.

Dictate instead of typing
=========================

A microphone button (:guilabel:`Dictate`) appears in the message box of the
chatter and of Discuss, also when you edit a message, and next to the input of
the AI panel. It is shown only to AI users, once a speech-to-text model is
configured and when your browser can record.

1. Click the microphone and allow the browser to use it when asked.
2. Speak. Click the button again (:guilabel:`Stop dictation`) when you are done,
   or wait for the maximum length.
3. The recognised text is inserted at the cursor. It is never sent
   automatically: read it, correct it and send it with the normal button.

The dictation audio is sent to the provider for transcription and is never
stored in eYssen.

Transcribe a call
=================

In a Discuss call, every participant sees the action :guilabel:`Transcribe` in
the call controls (or :guilabel:`Join transcription` once someone has started
it, and :guilabel:`Stop transcription` while you take part). While a call is
being transcribed, the action is highlighted for everyone.

How consent works
-----------------

Transcription is opt-in for each person:

- Turning it on asks you to confirm that your microphone will be recorded and
  transcribed.
- When the first participant starts the transcription, a notice is posted in the
  channel. It says who started it, that only people who turn it on themselves
  are recorded, each from their own microphone, and how long the audio is kept.
  Everyone who joins later is announced the same way.
- Each browser records only its own microphone, and only while that person has
  it turned on and is not muted. The server refuses audio from people who did
  not opt in and from people outside the channel.
- Turning it off, leaving the call or the end of the call stops your recording.
  Guests who are not users cannot take part.

.. important::
   Check the privacy and employment rules that apply to you before you use call
   transcription, and tell the people on your calls. The audio is sent to the
   speech-to-text provider you configured.

Transcript, summary and action items
------------------------------------

When the last person turns transcription off, or nobody is left in the call, the
transcript ends. If :guilabel:`Summarize calls automatically` is on, a summary
is posted in the channel about a minute later, as a comment from the person who
started the transcription. It contains the summary, the action items with a
suggested person and a link to the transcript.

Open all transcripts in :menuselection:`AI --> Call transcripts`. Members of the
channel see their own calls; AI administrators see all of them. On a transcript
you have the tabs :guilabel:`Summary` and :guilabel:`Transcript`, the list of
:guilabel:`Action items` and the buttons :guilabel:`Summarize` or
:guilabel:`Summarize again` if you want a summary on demand (not while the call
is still being recorded). Filter the list with :guilabel:`I took part` and
:guilabel:`Not summarized`.

The AI only suggests an assignee when the name spoken in the call matches
exactly one internal member of the channel. Nothing is scheduled automatically:
review the items on the transcript, edit the task, person or due date, tick the
ones you want and click :guilabel:`Create activities`. Your click is the
confirmation. Every item with an assignee gets a To-Do activity; the assignee
must be a channel member.

Limits
======

- Words spoken across the boundary of two pieces of audio can be split, and a
  single browser records one speaker only.
- Very long calls are summarised from the last 60,000 characters of the
  transcript.
- The push-to-talk and voice-activation settings of the call are not mirrored;
  only the mute state is respected.
