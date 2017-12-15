// @flow
import React from 'react'
import { WidgetGroup } from 'components'
import type { MetricSummary } from 'flow/types'

type Props = {
  community: string,
  metricSummaries: Array<MetricSummary>
}

const DashboardView = (props: Props) => {
  const {community, metricSummaries} = props
  return (
    <div>
      <h1>{community}</h1>
      <WidgetGroup metricSummaries={metricSummaries} />
    </div>
  )
}

export default DashboardView