// @flow
import React from 'react'
import { Widget } from 'components'
import CommunityPanel from './CommunityPanel'
import type { Community, Metric } from 'types'
import s from './DashboardView.module.css'

type Props = {
  community: Community,
  metrics: Array<Metric>
}

const DashboardView = ({community, metrics}: Props) => [
  <CommunityPanel community={community} key={1} />,
  <ul className={s.widgetsContainer} key={2}>
    {metrics.map((metric, index) => (
      <Widget metric={metric} key={index} />
    ))}
  </ul>
]

export default DashboardView
