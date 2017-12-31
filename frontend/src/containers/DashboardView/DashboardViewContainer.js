// @flow
import React, { Component } from 'react'
import { DashboardView } from 'components'
import type { Community, Metric } from 'flow/types'
import { getMetricSummaries } from 'utils/api'
import { mockMetrics } from 'utils/mock'
import { withLoadingAndError } from 'decorators'

type Props = {
  community: Community
}

type State = {
  isLoading: boolean,
  isError: boolean,
  metrics: Array<Metric>
}

class DashboardViewContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    metrics: []
  }

  componentDidMount () {
    const {community} = this.props
    getMetricSummaries(community.name)
      .then((data) => {
        this.setState({
          metrics: data.metrics,
          isLoading: false,
        })
      })
      .catch((error) => {
        this.setState({
          metrics: mockMetrics(), // TODO: just for demo
          isLoading: false,
          isError: false // TODO: just for demo
        })
      })
  }

  resetState = () => {
    this.setState({
      metrics: [],
      isLoading: true,
      isError: false
    })
  }

  @withLoadingAndError('There was an error.')
  render () {
    const {community} = this.props
    return (
      <DashboardView community={community} {...this.state} />
    )
  }
}

export default DashboardViewContainer