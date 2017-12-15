// @flow
import axios from 'axios'

export const getMetricSummaries = (community: string) => {
  const api = `/api/metric_summaries/${community}`
  return getRequest(api)
}

const getRequest = (api: string) => {
  return axios.get(api)
    .then(info => info.data)
    .catch(error => error.status)
}