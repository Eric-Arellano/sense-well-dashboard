// @flow
import type { MetricSummary } from 'flow/types'

export const mockMetricSummaries = () => {

  const widget1: MetricSummary = {
    name: "Water flow",
    unit: "L/hr",
    date: new Date(2017, 4, 11),
    currentValue: 43,
    average: 73,
    threshold: (value) => value > 20,
    thresholdText: "> 20"
  }

  const widget2: MetricSummary = {
    name: "Turbidity",
    unit: "%",
    date: new Date(2017, 8, 17),
    currentValue: 65,
    average: 32,
    threshold: (value) => value < 33,
    thresholdText: "< 33%"
  }

  const widget3: MetricSummary = {
    name: "Salinity",
    unit: "μS/cm",
    date: new Date(2017, 9, 14),
    currentValue: 0.41,
    average: 0.84,
    threshold: (value) => value < 0.6,
    thresholdText: "< 0.6"
  }

  return [widget1, widget2, widget3]
}