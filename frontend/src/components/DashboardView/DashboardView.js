// @flow
import React from 'react'
import { Widget } from 'components'
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
      <div>
        {metricSummaries.map((metric, index) => (
          <div key={index} xs="12" sm="6" lg="3">
            <Widget metricSummary={metric}/>
          </div>
        ))}
      </div>
      <div>
        <div xs={"24"} sm={"12"} lg={"6"}>
          {/*<Chart />*/}
        </div>
      </div>
    </div>
  )
}

export default DashboardView