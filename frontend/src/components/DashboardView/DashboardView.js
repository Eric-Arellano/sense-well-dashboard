// @flow
import React from 'react'
import { WidgetGroup } from 'components'
import type { Community, MetricSummary } from 'flow/types'
import CommunityPanel from '../Panel/CommunityPanel'

type Props = {
  community: Community,
  metricSummaries: Array<MetricSummary>
}

const DashboardView = (props: Props) => {
  const {community, metricSummaries} = props
  return [
    <CommunityPanel community={community} key={1} />,
    <WidgetGroup metricSummaries={metricSummaries} key={2} />
  ]
}

export default DashboardView