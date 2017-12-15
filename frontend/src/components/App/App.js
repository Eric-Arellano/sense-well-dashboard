// @flow
import React from 'react'
import { Footer, Header } from 'components'
import { DashboardViewContainer } from 'containers'
import type { Community } from 'flow/types'
import s from './App.module.css'

type Props = {
  community: Community
}

const App = (props: Props) => {
  const {community} = props
  return (
    <div className={s.app}>
      <Header />
      <div className={s.body}>
        <DashboardViewContainer community={community} />
      </div>
      <Footer />
    </div>
  )
}

export default App