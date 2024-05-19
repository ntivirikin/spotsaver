interface HomePageProps {
    onCreateClick: () => void
}

const HomePage = ( {onCreateClick}: HomePageProps ): JSX.Element => {
    return (
        <>
        <h1>SpotSaver</h1>
        <div className="map-buttons">
            <button>
            Mosquito Lake
            </button>
            <button>
            Winding Rivulet
            </button>
            <button>
            Old Burg Lake
            </button>
        </div>

        <div className="card">
            <button onClick={onCreateClick} >
            Log New Spot
            </button>
            <p>
            No spots found, please create one above!
            </p>
        </div>
        </>
    )
}

export default HomePage