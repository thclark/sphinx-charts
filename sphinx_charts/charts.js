function setPlaceholderError(placeholder, message) {
  if (!placeholder) {
    return
  }

  placeholder.style.color = 'red'

  const messageElement = placeholder.querySelector('span') || placeholder
  messageElement.textContent = message
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('div.sphinx-charts-chart').forEach(function (chart) {
    // TODO There has just *GOT* to be a better way of getting metadata from a sphinx directive int javascript than this
    const idPrefix = 'sphinx-charts-chart-id-'
    const uriPrefix = 'sphinx-charts-chart-uri-'
    const dnPrefix = 'sphinx-charts-chart-dn-'
    const classes = Array.from(chart.classList)
    let id
    let uri
    let dn

    classes.forEach(function (clazz) {
      if (clazz.startsWith(idPrefix)) {
        id = clazz.substring(idPrefix.length)
      } else if (clazz.startsWith(uriPrefix)) {
        uri = clazz.substring(uriPrefix.length)
      } else if (clazz.startsWith(dnPrefix)) {
        dn = clazz.substring(dnPrefix.length)
      }
    })

    const placeholder = document.querySelector(`div.sphinx-charts-placeholder-${id}`)

    const config = {
      // toImageButtonOptions: {
      //   format: 'svg', // one of png, svg, jpeg, webp
      //   filename: dn,
      // },
      displaylogo: false,
      automargin: true,
      responsive: true,
    }

    fetch(uri)
      .then(function (response) {
        if (!response.ok) {
          throw new Error(`Cannot load figure data from ${uri}`)
        }
        return response.json()
      })
      .then(function (fetched) {
        try {
          // Generate plotly figure and remove the placeholder, or show error if we can't render
          console.log('Successfully fetched data for chart id ', id, uri)
          // window.PlotlyConfig = { MathJaxConfig: 'local' }
          Plotly.newPlot(
            document.getElementById(`sphinx-charts-chart-id-${id}`),
            fetched.data,
            fetched.layout,
            config
          )
          if (placeholder) {
            placeholder.style.display = 'none'
          }
        } catch (err) {
          setPlaceholderError(
            placeholder,
            'Chart data or layout does not work with Plotly.js v2.11.1!!!'
          )
        }
      })
      .catch(function () {
        setPlaceholderError(placeholder, 'Cannot load figure data!!!')
        console.log('Error retrieving data for chart id', id, uri)
      })
  })
})
