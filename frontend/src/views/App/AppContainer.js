// @flow
import React, { Component } from 'react'
import AppView from './AppView'
import type { Community } from 'types'
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
    return <AppView {...this.state} />
  }
}

export default AppContainer;
