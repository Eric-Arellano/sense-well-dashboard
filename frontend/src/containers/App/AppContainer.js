// @flow
import React, { Component } from 'react'
import { App } from 'components'
import type { Community } from 'flow/types'
import { mockCommunity } from 'utils/mock'

type Props = { }

type State = {
  community: Community
}

class AppContainer extends Component<Props, State> {

  state = {
    community: mockCommunity()
  }

  render() {
    return <App {...this.state} />
  }
}

export default AppContainer;
