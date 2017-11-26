// @flow
import React from 'react'
import { Switch, Route, Redirect } from 'react-router-dom';
import { Container } from 'reactstrap'
import { Header, Sidebar, Breadcrumb, Aside, Footer } from 'components'
import { DashboardContainer } from 'containers'

const App = () => {
  return (
    <div className="app">
      <Header />
      <div className="app-body">
        <Sidebar />
        <main className="main">
          <Breadcrumb />
          <Container fluid>
            <Switch>
              <Route path="/dashboard" name="Dashboard" component={DashboardContainer}/>
              <Redirect from="/" to="/dashboard"/>
            </Switch>
          </Container>
        </main>
        <Aside />
      </div>
      <Footer />
    </div>
  )
}

export default App