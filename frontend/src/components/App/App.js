// @flow
import React from 'react'
import { Footer, Header } from 'components'
import { DashboardViewContainer } from 'containers'
import type { Community } from 'flow/types'
import s from './App.module.css'

type Props = {
  community: Community
}

const App = ({ community }: Props) => {
  return (
    <div className={s.app}>
      <Header />
      <main className={s.body}>
        <DashboardViewContainer community={community} />
      </main>
      <Footer />
    </div>
  )
}

export default App
