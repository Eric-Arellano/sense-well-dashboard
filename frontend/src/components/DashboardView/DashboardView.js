// @flow
import React from 'react'
import { WidgetGroup } from 'components'
import type { Community, MetricSummary } from 'flow/types'

type Props = {
  community: Community,
  metricSummaries: Array<MetricSummary>
}

const DashboardView = (props: Props) => {
  const {community, metricSummaries} = props
  return (
    <div>
      <h1>{community.name}</h1>
      <WidgetGroup metricSummaries={metricSummaries} />
    </div>
  )
}

export default DashboardView