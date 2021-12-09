Module(
    body=[
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='tagged', asname=None),
                alias(name='HttpCase', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestUiSession',
            bases=[Name(id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_admin_survey_session',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method tests a full \'survey session\' flow.\n        Break down of different steps:\n        - Create the test data\n          - A scored survey\n          - A nickname question\n          - "Simple" type questions (text, date, datetime)\n          - A regular simple choice\n          - A scored simple choice\n          - A scored AND timed multiple choice\n        - Create a new survey session\n        - Register 3 attendees to it\n        - Open the session manager to check that our attendees are accounted for\n        - Create some answers to our survey questions.\n        - Then run the \'big\' manage session tour (see JS doc for details)\n        - And finally check that our session and attendees inputs are correctly closed. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='test_start_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='survey_session', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.survey', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='access_token', kind=None),
                                            Constant(value='access_mode', kind=None),
                                            Constant(value='users_can_go_back', kind=None),
                                            Constant(value='questions_layout', kind=None),
                                            Constant(value='scoring_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='User Session Survey', kind=None),
                                            Constant(value='b137640d-14d4-4748-9ef6-344caaaaafe', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='page_per_question', kind=None),
                                            Constant(value='scoring_without_answers', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nickname_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='save_as_nickname', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Nickname', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='char_box', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='text_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Text Question', kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value='char_box', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Date Question', kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='datetime_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Datetime Question', kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value='datetime', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='simple_choice_answer_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value='First', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='simple_choice_answer_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value='Second', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='simple_choice_answer_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value='Third', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='simple_choice_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='suggested_answer_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Regular Simple Choice', kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value='simple_choice', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='simple_choice_answer_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='simple_choice_answer_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='simple_choice_answer_3', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='scored_choice_answer_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='is_correct', kind=None),
                                            Constant(value='answer_score', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Correct', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='scored_choice_answer_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value='Incorrect 1', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='scored_choice_answer_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value='Incorrect 2', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='scored_choice_answer_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value='Incorrect 3', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='scored_choice_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='suggested_answer_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Scored Simple Choice', kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value='simple_choice', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='scored_choice_answer_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='scored_choice_answer_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='scored_choice_answer_3', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='scored_choice_answer_4', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timed_scored_choice_answer_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='is_correct', kind=None),
                                            Constant(value='answer_score', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Correct', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timed_scored_choice_answer_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='is_correct', kind=None),
                                            Constant(value='answer_score', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Also correct but less points', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timed_scored_choice_answer_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question.answer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='answer_score', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Incorrect', kind=None),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=40, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timed_scored_choice_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='is_time_limited', kind=None),
                                            Constant(value='time_limit', kind=None),
                                            Constant(value='suggested_answer_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Timed Scored Multiple Choice', kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value='multiple_choice', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=1, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='timed_scored_choice_answer_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='timed_scored_choice_answer_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='timed_scored_choice_answer_3', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='action_open_session_manager_mock',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='self', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Mock original method to ensure we are not using another tab\n            as it creates issues with automated tours. ', kind=None),
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='target', kind=None),
                                            Constant(value='url', kind=None),
                                        ],
                                        values=[
                                            Constant(value='ir.actions.act_url', kind=None),
                                            Constant(value='Open Session Manager', kind=None),
                                            Constant(value='self', kind=None),
                                            BinOp(
                                                left=Constant(value='/survey/session/manage/%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='access_token',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[
                                            Constant(value='odoo.addons.survey.models.survey_survey.Survey.action_open_session_manager', kind=None),
                                            Name(id='action_open_session_manager_mock', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='start_tour',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/web', kind=None),
                                            Constant(value='test_survey_session_create_tour', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='login',
                                                value=Constant(value='admin', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey_session', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='session_start_time', kind=None)],
                                        values=[
                                            BinOp(
                                                left=Name(id='test_start_time', ctx=Load()),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='minutes',
                                                            value=Constant(value=10, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='attendee_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey_session', ctx=Load()),
                                    attr='_create_answer',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attendee_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey_session', ctx=Load()),
                                    attr='_create_answer',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attendee_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey_session', ctx=Load()),
                                    attr='_create_answer',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_attendees', ctx=Store())],
                            value=List(
                                elts=[
                                    Name(id='attendee_1', ctx=Load()),
                                    Name(id='attendee_2', ctx=Load()),
                                    Name(id='attendee_3', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ready', kind=None),
                                    Attribute(
                                        value=Name(id='survey_session', ctx=Load()),
                                        attr='session_state',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='attendee', ctx=Load()),
                                                    attr='is_session_answer',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='attendee', ctx=Store()),
                                                        iter=Name(id='all_attendees', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Created answers should be within the session.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='attendee', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='new', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='attendee', ctx=Store()),
                                                        iter=Name(id='all_attendees', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value="Created answers should be in the 'new' state.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[
                                            Constant(value='odoo.addons.survey.models.survey_survey.Survey.action_open_session_manager', kind=None),
                                            Name(id='action_open_session_manager_mock', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='start_tour',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/web', kind=None),
                                            Constant(value='test_survey_session_start_tour', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='login',
                                                value=Constant(value='admin', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='in_progress', kind=None),
                                    Attribute(
                                        value=Name(id='survey_session', ctx=Load()),
                                        attr='session_state',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='session_start_time',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_1', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='nickname_question', ctx=Load()),
                                    Constant(value='xxxTheBestxxx', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_2', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='nickname_question', ctx=Load()),
                                    Constant(value='azerty', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_3', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='nickname_question', ctx=Load()),
                                    Constant(value='nicktalope', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='xxxTheBestxxx', kind=None),
                                    Attribute(
                                        value=Name(id='attendee_1', ctx=Load()),
                                        attr='nickname',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='azerty', kind=None),
                                    Attribute(
                                        value=Name(id='attendee_2', ctx=Load()),
                                        attr='nickname',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='nicktalope', kind=None),
                                    Attribute(
                                        value=Name(id='attendee_3', ctx=Load()),
                                        attr='nickname',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_1', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='text_question', ctx=Load()),
                                    Constant(value='Attendee 1 is the best', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_2', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='text_question', ctx=Load()),
                                    Constant(value='Attendee 2 rulez', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_3', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='text_question', ctx=Load()),
                                    Constant(value='Attendee 3 will crush you', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_1', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='date_question', ctx=Load()),
                                    Constant(value='2010-10-10', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_2', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='date_question', ctx=Load()),
                                    Constant(value='2011-11-11', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_2', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='datetime_question', ctx=Load()),
                                    Constant(value='2010-10-10 10:00:00', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_3', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='datetime_question', ctx=Load()),
                                    Constant(value='2011-11-11 15:55:55', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_1', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='simple_choice_question', ctx=Load()),
                                    Attribute(
                                        value=Name(id='simple_choice_answer_1', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_2', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='simple_choice_question', ctx=Load()),
                                    Attribute(
                                        value=Name(id='simple_choice_answer_1', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_3', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='simple_choice_question', ctx=Load()),
                                    Attribute(
                                        value=Name(id='simple_choice_answer_2', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_1', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='scored_choice_question', ctx=Load()),
                                    Attribute(
                                        value=Name(id='scored_choice_answer_1', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_2', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='scored_choice_question', ctx=Load()),
                                    Attribute(
                                        value=Name(id='scored_choice_answer_2', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_3', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='scored_choice_question', ctx=Load()),
                                    Attribute(
                                        value=Name(id='scored_choice_answer_3', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_1', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='timed_scored_choice_question', ctx=Load()),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='timed_scored_choice_answer_1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='timed_scored_choice_answer_3', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_2', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='timed_scored_choice_question', ctx=Load()),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='timed_scored_choice_answer_1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='timed_scored_choice_answer_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attendee_3', ctx=Load()),
                                    attr='save_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='timed_scored_choice_question', ctx=Load()),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='timed_scored_choice_answer_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[
                                            Constant(value='odoo.addons.survey.models.survey_survey.Survey.action_open_session_manager', kind=None),
                                            Name(id='action_open_session_manager_mock', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='start_tour',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/web', kind=None),
                                            Constant(value='test_survey_session_manage_tour', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='login',
                                                value=Constant(value='admin', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='survey_session', ctx=Load()),
                                                attr='session_state',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='answer', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='done', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='answer', ctx=Store()),
                                                        iter=Name(id='all_attendees', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
