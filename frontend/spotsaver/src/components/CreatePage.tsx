import './CreatePage.css'

interface CreatePageProps {
    onBackClick: () => void
}

const CreatePage = ( {onBackClick}: CreatePageProps ): JSX.Element => {
    return (
        <>
        <div className="create-forms">
            <span>Map Name</span>
            <input></input>
            <span>Co-ordinates</span>
            <div className="cords-buttons">
                <input></input><input></input>
            </div>
            <span>Clip</span>
            <input></input>
            <span>Bait</span>
            <input></input>
        </div>

        <button>Create</button>
        <button className="back-button" onClick={onBackClick}>Back</button>
        </>
    )

}

export default CreatePage