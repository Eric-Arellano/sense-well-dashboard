// @flow

export type MetricSummary = {
  name: string,
  unit: string,
  currentValue: number,
  date: Date,
  average: number,
  threshold: (number) => boolean,
  thresholdText: string
}