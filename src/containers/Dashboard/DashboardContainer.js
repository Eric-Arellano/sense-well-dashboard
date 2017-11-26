// @flow
import React, { Component } from 'react'
import { Dashboard } from 'components'
import type { MetricSummary } from '../../flow/types'
import { mockMetricSummaries } from 'data/mock'

type Props = { }

type State = {
  metricSummaries: Array<MetricSummary>
}

class DashboardContainer extends Component<Props, State> {

  state = {
    metricSummaries: mockMetricSummaries()
  }

  render() {
    const { metricSummaries } = this.state
    return (
        <Dashboard metricSummaries={metricSummaries}/>
      )
  }
}

export default DashboardContainer