Module(
    body=[
        ImportFrom(
            module='odoo.addons.survey.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSurveyFlowWithConditions',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TestSurveyCommon',
                    ctx=Load(),
                ),
                Name(id='HttpCase', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_conditional_flow_with_scoring',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='survey_user', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='survey', ctx=Store())],
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
                                                    Constant(value='access_mode', kind=None),
                                                    Constant(value='questions_layout', kind=None),
                                                    Constant(value='scoring_type', kind=None),
                                                    Constant(value='scoring_success_min', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Survey', kind=None),
                                                    Constant(value='public', kind=None),
                                                    Constant(value='page_per_section', kind=None),
                                                    Constant(value='scoring_with_answers', kind=None),
                                                    Constant(value=85.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page_0', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
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
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='survey_manager',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='survey_id', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='is_page', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='First page', kind=None),
                                                    Attribute(
                                                        value=Name(id='survey', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='q01', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Question 1', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 2', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 3', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Answer 4', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='q02', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Question 2', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='is_conditional',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='triggering_question_id',
                                                value=Attribute(
                                                    value=Name(id='q01', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='triggering_answer_id',
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='q01', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='q', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Attribute(
                                                                    value=Name(id='q', ctx=Load()),
                                                                    attr='is_correct',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Answer 2', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 3', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 4', kind=None)],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='q03', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Question 3', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 2', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 3', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Answer 4', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Question 4', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='is_conditional',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='triggering_question_id',
                                                value=Attribute(
                                                    value=Name(id='q03', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='triggering_answer_id',
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='q03', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='q', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Attribute(
                                                                    value=Name(id='q', ctx=Load()),
                                                                    attr='is_correct',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Answer 2', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 3', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 4', kind=None)],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='q05', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Question 5', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 2', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 3', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Answer 4', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='q06', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='Question 6', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please select an answer', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='is_conditional',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='triggering_question_id',
                                                value=Attribute(
                                                    value=Name(id='q05', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='triggering_answer_id',
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='q05', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='q', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Attribute(
                                                                    value=Name(id='q', ctx=Load()),
                                                                    attr='is_correct',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 1', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Answer 2', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Constant(value=1.0, kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 3', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='Answer 4', kind=None)],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_start',
                                    ctx=Load(),
                                ),
                                args=[Name(id='survey', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user_inputs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='survey_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='survey', ctx=Load()),
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
                                keywords=[],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='user_inputs', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='answer_token', ctx=Store())],
                            value=Attribute(
                                value=Name(id='user_inputs', ctx=Load()),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_page',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='csrf_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_csrf_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_begin',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='r', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='answers', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Name(id='q01', ctx=Load()),
                                    Name(id='q02', ctx=Load()),
                                    Name(id='q03', ctx=Load()),
                                    Name(id='q05', ctx=Load()),
                                    Name(id='q06', ctx=Load()),
                                ],
                                values=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='q01', ctx=Load()),
                                            attr='suggested_answer_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=3, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='q02', ctx=Load()),
                                            attr='suggested_answer_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='q03', ctx=Load()),
                                            attr='suggested_answer_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='q05', ctx=Load()),
                                            attr='suggested_answer_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=3, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='q06', ctx=Load()),
                                            attr='suggested_answer_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_answer_page',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page_0', ctx=Load()),
                                    Name(id='answers', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                    Name(id='csrf_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_inputs', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='user_inputs', ctx=Load()),
                                                attr='scoring_percentage',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=60, kind=None),
                                    Constant(value='Three right answers out of five (the fourth one is still hidden)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='user_inputs', ctx=Load()),
                                        attr='scoring_success',
                                        ctx=Load(),
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
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='functional', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
