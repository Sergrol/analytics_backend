import React from 'react';
import get from 'lodash/get';
import {shallowEqual} from "recompose";

import {SortableContainer, SortableElement, SortableHandle} from 'react-sortable-hoc';

import TableContainer from "@material-ui/core/TableContainer";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableCell from "@material-ui/core/TableCell";

import Paper from "@material-ui/core/Paper";
import Button from '@material-ui/core/Button';
import AddIcon from '@material-ui/icons/Add';
import withStyles from '@material-ui/core/styles/withStyles';
import DragIndicatorIcon from '@material-ui/icons/DragIndicator';

import EditedRow from "./EditedRow";

import {ThirdStepProps} from './types';

import connect from './ThirdStep.connect';
import styles from './ThirdStep.styles';
import {workProgramSectionFields} from "../enum";
import Select from "@material-ui/core/Select";

class ThirdStep extends React.Component<ThirdStepProps> {
    state = {
        createNewSectionMode: false
    }

    componentDidUpdate(prevProps: Readonly<ThirdStepProps>, prevState: Readonly<{}>, snapshot?: any) {
        if (!shallowEqual(this.props.sections, prevProps.sections)){
            this.setState({sections: this.props.sections});
        }
    }

    getNewSection = () => ({
        name: '',
        SRO: '',
        contact_work: '',
        lecture_classes: '',
        practical_lessons: '',
        total_hours: '',
        laboratory: '',
        ordinal_number: get(this, 'props.sections.length', 0) + 1 ,
    })

    handleCreateNewSection = () => {
        this.setState({
            createNewSectionMode: true,
        });

    };

    removeNewSection = () => {
        this.setState({
            createNewSectionMode: false,
        });
    }

    onSortEnd = ({oldIndex, newIndex}: any) => {
        const {sections} = this.props;
        let currentSection = {...sections[oldIndex]};

        currentSection[workProgramSectionFields.ORDINAL_NUMBER] = newIndex + 1;

        this.props.actions.saveSection(currentSection);
    }

    render() {
        // @ts-ignore
        const {classes, sections} = this.props;
        const {createNewSectionMode} = this.state;

        return (
            <div className={classes.thirdStep}>
                <TableContainer component={Paper}>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell className={classes.headerCell} rowSpan={2} colSpan={2}> № раздела </TableCell>
                                <TableCell className={classes.headerCell} rowSpan={2}>Наименование раздела дисциплины</TableCell>
                                <TableCell className={classes.headerCell} colSpan={6}>Распределение часов по дисциплине</TableCell>
                                <TableCell className={classes.headerCell} rowSpan={2}> </TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell className={classes.headerCell}>Контактная работа</TableCell>
                                <TableCell className={classes.headerCell}>Занятия лекционного типа</TableCell>
                                <TableCell className={classes.headerCell}>Лабораторные занятия</TableCell>
                                <TableCell className={classes.headerCell}>Практические занятия</TableCell>
                                <TableCell className={classes.headerCell}>СРО</TableCell>
                                <TableCell className={classes.headerCell}>Всего часов</TableCell>
                            </TableRow>
                        </TableHead>

                        <SortableList sections={sections}
                                      useDragHandle={true}
                                      hideSortableGhost={false}
                                      removeNewSection={this.removeNewSection}
                                      onSortEnd={this.onSortEnd}
                        />

                        {createNewSectionMode &&
                            <TableRow>
                                <TableCell />
                                <EditedRow section={this.getNewSection()} removeNewSection={this.removeNewSection}/>
                            </TableRow>
                        }
                    </Table>
                </TableContainer>

                {!createNewSectionMode
                    && <Button color="primary"
                               variant="outlined"
                               className={classes.addIcon}
                               onClick={this.handleCreateNewSection}
                        >
                        <AddIcon/>
                        Добавить раздел
                    </Button>
                }
            </div>
        );
    }
}

const DragHandle = SortableHandle(() => <DragIndicatorIcon />);

// @ts-ignore
const SortableItem = SortableElement(({section, removeNewSection}) =>
    <TableRow>
        <TableCell style={{backgroundColor: '#fff'}} >
            <DragHandle />
        </TableCell>
        <EditedRow section={section} removeNewSection={removeNewSection}/>
    </TableRow>
);

// @ts-ignore
const SortableList = SortableContainer(({sections, removeNewSection}) => {
    return (<TableBody>
            {sections.map((value: any, index: number) => (
                <SortableItem key={`item-${index}`}
                              index={index}
                              section={value}
                              removeNewSection={removeNewSection}
                />
            ))}
        </TableBody>
    );
});

// @ts-ignore
export default connect(withStyles(styles)(ThirdStep));