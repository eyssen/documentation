====================
Providers and models
====================

eYssen AI talks to language-model providers over their web APIs. This page
explains what to configure once, so that every other AI feature (chat, writing
assistant, knowledge sources, voice, images) has a model to work with.

Providers
=========

Open :menuselection:`AI --> Configuration --> Providers --> LLM Providers` and
create one provider per account you use. The supported types are OpenRouter,
OpenAI, Anthropic, xAI and Google Gemini; any OpenAI-compatible gateway works
through the :guilabel:`Base Url` field. The API key is write-only: once saved it
is never shown again.

A hosted provider needs its API key. If it has none, the request fails at once
with the message "The AI provider has no API key. Set it under AI >
Configuration > Providers." instead of being sent and rejected by the provider.
A self-hosted endpoint such as Ollama, LM Studio or vLLM needs no key. That is
the case when the :guilabel:`Base Url` points to the local machine
(``localhost``), to a private network address, to a name ending in ``.local``,
``.localhost``, ``.internal`` or ``.lan``, or to a plain host name without dots,
such as ``http://ollama:11434/v1``.

Click :guilabel:`Refresh Models` on the provider to import its model catalogue
(and prices where the provider publishes them). Refreshing never overwrites a
price you entered by hand.

Kinds of models
===============

Every model has a :guilabel:`Kind`. The kind decides where the model can be
chosen:

- :guilabel:`Chat` models answer conversations and drive the assistant, the
  writing assistant and all the one-click features. Choose one under
  :menuselection:`AI --> Configuration --> Settings` in :guilabel:`AI Model`.
  The assistant calls tools, so pick a model that supports tool calling.
- :guilabel:`Image generation` models create pictures for the AI panel, the
  editor and the product and Knowledge cover features. Set the model by hand to
  this kind, then pick it in :guilabel:`Image Model` under :menuselection:`AI
  --> Configuration --> Settings`. Anthropic offers no image models; use another
  provider for images.
- :guilabel:`Embedding` models turn text into vectors for knowledge sources and
  similar tasks (see :doc:`knowledge_sources`). OpenAI, Google Gemini and
  OpenRouter provide them; xAI and Anthropic do not.
- :guilabel:`Speech to text` models transcribe audio for dictation and call
  transcription (see :doc:`voice`). Any provider with an OpenAI-compatible audio
  transcription route works, including a custom base URL such as Groq or a
  self-hosted Whisper server. Anthropic and OpenRouter are refused.

What Refresh Models does for each kind
======================================

- Models whose id contains ``embed`` are filed as :guilabel:`Embedding`
  automatically and never offered to the chat loop. OpenRouter lists embedding
  models on a separate endpoint, so a refresh of an OpenRouter provider also
  fetches that list and adds those models; if that second request fails, the
  normal refresh still succeeds.
- Models whose id contains ``whisper`` or ``transcribe`` are filed as
  :guilabel:`Speech to text`.
- Image models are not detected: open the model and set its :guilabel:`Kind` to
  :guilabel:`Image generation` yourself. A refresh never changes a kind you set
  by hand.

Where each model is chosen
==========================

- :guilabel:`AI Model` and :guilabel:`Image Model`: :menuselection:`AI -->
  Configuration --> Settings`, block :guilabel:`Model`.
- :guilabel:`Embedding model`: same page, block :guilabel:`Knowledge sources`.
- :guilabel:`Speech-to-text model`: same page, block :guilabel:`Voice`.

Reasoning and cost
==================

Only models flagged as reasoning-capable react to :guilabel:`Think longer` in
the AI panel (see :doc:`panel`). Flag a model only if its API documents a
reasoning effort or a thinking budget: other models reject the extra parameter.

Each model has unit prices (per million tokens, per image or per audio minute).
They feed the cost cap in the settings and the log entries. A model without
prices is not blocked, but the cost cap cannot count it.

.. important::
   Everything a model is asked is sent to the provider you chose. Pick providers
   whose data terms fit your obligations, and keep the log level on
   :guilabel:`Ai Log Level` metadata only unless you need payloads.
