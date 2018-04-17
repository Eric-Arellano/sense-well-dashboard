// @flow
import React from 'react'
import type { Community } from 'flow/types'
import { Entry, Panel } from 'components'

type Props = {
  community: Community
}

const CommunityPanel = ({community: {name, latitude, longitude, size, installation, lastInspection}}: Props) => (
  <Panel header={name}>
    <Entry>Latitude: {latitude}</Entry>
    <Entry>Longitude: {longitude}</Entry>
    <Entry>Size of community: {size} people</Entry>
    <Entry>Installation date: {installation.toDateString()}</Entry>
    <Entry>Last inspection date: {lastInspection.toDateString()}</Entry>
  </Panel>
)

export default CommunityPanel
