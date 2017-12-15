// @flow
import React, { Component } from 'react'
import { DashboardView } from 'components'
import type { Community, MetricSummary } from '../../flow/types'
import { getMetricSummaries } from '../../utils/api'
import { mockMetricSummaries } from 'utils/mock'

type Props = {
  community: Community
}

type State = {
  isLoading: boolean,
  isError: boolean,
  metricSummaries: Array<MetricSummary>
}

class DashboardViewContainer extends Component<Props, State> {

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
    const {community} = this.props
    return (
      <DashboardView community={community} {...this.state} />
    )
  }
}

export default DashboardViewContainer