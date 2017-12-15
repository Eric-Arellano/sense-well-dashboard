// @flow
import React from 'react'
import type { MetricSummary } from 'flow/types'
import { Widget } from 'components'
import s from './WidgetGroup.module.css'

type Props = {
  metricSummaries: Array<MetricSummary>
};

const WidgetGroup = (props: Props) => {
  const {metricSummaries} = props
  return (
    <div className={s.container}>
      {metricSummaries.map((metric, index) => (
        <Widget metricSummary={metric} key={index} />
      ))}
    </div>
  )
}

export default WidgetGroup