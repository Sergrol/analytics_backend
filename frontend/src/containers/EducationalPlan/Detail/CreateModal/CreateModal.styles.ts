import {createStyles, Theme} from "@material-ui/core";

export default (theme: Theme) => createStyles({
    dialogContent: {
        display: 'flex',
        padding: 48
    },
    label: {
        fontSize: '14px',
        marginBottom: 10
    },
    addWorkProgramButton: {
        marginLeft: 'auto',
        padding: 0,
        '&:hover': {
            background: 'none'
        }
    },
    leftSide: {
        width: '50%',
        maxWidth: '550px',
        flex: 'none'
    },
    rightSide: {
        width: '100%',
        paddingLeft: '50px',
        paddingRight: '20px',
        boxSizing: 'border-box'
    },
    semesterField: {
        width: '100px',
        marginBottom: '10px',
        marginRight: '10px',
        '& .MuiInputLabel-outlined': {
            fontSize: '13px'
        },
        '& .MuiOutlinedInput-notchedOutline legend': {
            width: '55px !important'
        }
    },
    workProgramList: {
        width: '100%',
        height: '100%'
    },
    appBar: {
        position: 'relative',
    },
    title: {
        marginLeft: theme.spacing(2),
        flex: 1,
    },
    semesterBlock: {
        maxWidth: '600px'
    },
    //@ts-ignore
    root: {
        //@ts-ignore
        zIndex: '10000 !important'
    },
    dialog: {
        boxSizing: 'border-box',
    },
    semesterList: {
        display: 'flex',
        justifyContent: 'space-between',
        flexWrap: 'wrap'
    },
    workProgramBlock: {
        marginBottom: 30
    },
    addWorkProgramButtonWrap: {
        display: 'flex'
    },
    workProgramItem: {
        display: 'flex',
        marginTop: 5,
        marginBottom: 5,
        '& svg': {
            cursor: 'pointer',
            '&:hover': {
                color: theme.palette.primary.main
            }
        }
    },
    input: {
        width: '550px',
    },
    lastInput: {
        width: '550px',
    },
    selector: {
        width: '550px'
    },
    actions: {
        padding: '15px 24px 20px'
    },
    marginBottom30: {
        marginBottom: '30px'
    },
    selectorWrap: {
        '& .MuiInputLabel-shrink': {
            transform: 'translate(14px, -6.5px) scale(0.75) !important',
        },
        '& .MuiOutlinedInput-notchedOutline legend': {
            width: '40px !important'
        }
    },
    radioGroup: {
        display: 'flex',
        flexDirection: 'row',
        marginBottom: '30px',
        width: '550px'
    },
    datePicker: {
        width: '100%'
    },
    workProgramBlockItem: {
        padding: 20,
        marginBottom: 40,
        boxShadow: '0px 0px 6px 1px rgba(194,194,194,0.3)',
    },
    smallButton: {
        cursor: 'pointer',
        color: theme.palette.primary.main,
        display: 'flex',
        alignItems: 'center'
    },
    deleteIcon: {
        cursor: "pointer",
        '&:hover': {
            color: theme.palette.primary.main,
        }
    },
    indicatorItem: {
        marginBottom: '10px',
        '& svg': {
            position: 'relative',
            top: '6px',
        }
    }
});