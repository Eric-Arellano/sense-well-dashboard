// @flow
import React, { Component } from 'react'
import { Dashboard } from 'components'
import type { MetricSummary } from '../../flow/types'
import { getMetricSummaries } from '../../utils/api'
import { mockMetricSummaries } from 'data/mock'

type Props = {
  community: string
}

type State = {
  isLoading: boolean,
  isError: boolean,
  metricSummaries: Array<MetricSummary>
}

class DashboardContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    metricSummaries: []
  }

  componentDidMount () {
    getMetricSummaries(this.props.community)
      .then((data) => {
        this.setState({
          metricSummaries: data.metricSummaries,
          isLoading: false,
        })
      })
      .catch((error) => {
        this.setState({
          metricSummaries: mockMetricSummaries(), // TODO: just for demo
          isLoading: false,
          isError: true
        })
      })
  }

  render () {
    return (
      <Dashboard {...this.state} />
    )
  }
}

export default DashboardContainer