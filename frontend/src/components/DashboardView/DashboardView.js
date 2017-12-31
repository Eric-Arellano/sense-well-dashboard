// @flow
import React from 'react'
import { ChartWidget, CommunityPanel, Widget } from 'components'
import type { Community, MetricSummary } from 'flow/types'
import s from './DashboardView.module.css'

type Props = {
  community: Community,
  metricSummaries: Array<MetricSummary>
}

const DashboardView = ({community, metricSummaries}: Props) => [
  <CommunityPanel community={community} key={1} />,
  <ul className={s.widgetsContainer} key={2}>
    {metricSummaries.map((metric, index) => (
      <Widget metricSummary={metric} key={index} />
    ))}
  </ul>,
  <ul className={s.chartsContainer} key={3}>
    <ChartWidget header={"Water flow"} key={4} />
    <ChartWidget header={"Turbidity"} key={5} />
    <ChartWidget header={"Salinity"} key={6} />
  </ul>
]

export default DashboardView
