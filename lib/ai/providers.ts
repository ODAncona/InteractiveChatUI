import {
  customProvider,
  extractReasoningMiddleware,
  wrapLanguageModel,
} from 'ai';
import { xai } from '@ai-sdk/xai';
import { cerebras } from '@ai-sdk/cerebras';
import { isTestEnvironment } from '../constants';
import {
  artifactModel,
  chatModel,
  reasoningModel,
  titleModel,
} from './models.test';

export const myProvider = isTestEnvironment
  ? customProvider({
      languageModels: {
        'chat-model': chatModel,
        'chat-model-reasoning': reasoningModel,
        'title-model': titleModel,
        'artifact-model': artifactModel,
      },
    })
  : customProvider({
      languageModels: {
        'chat-model': cerebras('llama3.1-8b'),
        'chat-model-reasoning': wrapLanguageModel({
          model: cerebras('llama3.1-8b'),
          middleware: extractReasoningMiddleware({ tagName: 'think' }),
        }),
        'title-model': cerebras('llama3.1-8b'),
        'artifact-model': cerebras('llama3.1-8b'),
      },
      imageModels: {
        'small-model': xai.image('grok-2-image'),
      },
    });
