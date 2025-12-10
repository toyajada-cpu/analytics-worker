// types.ts

import { Writable } from 'stream';

interface AnalyticsEvent {
  id: string;
  timestamp: Date;
  source: string;
  data: Record<string, string>;
}

interface AnalyticsWorkerOptions {
  maxRetries?: number;
  timeout?: number;
}

interface AnalyticsWorkerQueueOptions {
  maxConcurrency?: number;
  maxRetries?: number;
  timeout?: number;
}

interface AnalyticsWorkerConfig {
  queueOptions: AnalyticsWorkerQueueOptions;
  workerOptions: AnalyticsWorkerOptions;
}

interface AnalyticsStreamOptions {
  concurrency?: number;
  timeout?: number;
  maxRetries?: number;
}

interface AnalyticsStreamOptionsWithFormat {
  format: string;
  concurrency?: number;
  timeout?: number;
  maxRetries?: number;
}

interface AnalyticsFormat {
  id: string;
  description: string;
  type: string;
  streams: string[];
  options: AnalyticsStreamOptionsWithFormat;
}

interface AnalyticsStream {
  id: string;
  description: string;
  type: string;
  format: AnalyticsFormat;
  options: AnalyticsStreamOptions;
  write(chunk: any): void;
  end(): void;
  destroy(): void;
}