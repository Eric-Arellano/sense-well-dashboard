// @flow
import React from 'react'
import { CommunityPanel, Widget } from 'components'
import type { Community, MetricSummary } from 'flow/types'
import s from './DashboardView.module.css'

type Props = {
  community: Community,
  metricSummaries: Array<MetricSummary>
}

const DashboardView = ({ community, metricSummaries }: Props) => [
  <CommunityPanel community={community} key={1} />,
  <ul className={s.widgetsContainer} key={2}>
    { metricSummaries.map((metric, index) => (
      <Widget {...metric} key={index} />
    ))}
  </ul>
]

export default DashboardView
