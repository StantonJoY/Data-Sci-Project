Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.survey.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='users', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSurveyInternals',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TestSurveyCommon',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_answer_validation_mandatory',
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
                            value=Constant(value=' For each type of question check that mandatory questions correctly check for complete answers ', kind=None),
                        ),
                        For(
                            target=Name(id='question', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_one_question_per_type',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertDictEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='validate_question',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='', kind=None)],
                                                keywords=[],
                                            ),
                                            Dict(
                                                keys=[
                                                    Attribute(
                                                        value=Name(id='question', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                values=[Constant(value='TestError', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='survey_manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_answer_validation_date',
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
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_question',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='page_0',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Q0', kind=None),
                                    Constant(value='date', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='validation_required',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='validation_min_date',
                                        value=Constant(value='2015-03-20', kind=None),
                                    ),
                                    keyword(
                                        arg='validation_max_date',
                                        value=Constant(value='2015-03-25', kind=None),
                                    ),
                                    keyword(
                                        arg='validation_error_msg',
                                        value=Constant(value='ValidationError', kind=None),
                                    ),
                                ],
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
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Is Alfred an answer ?', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This is not a date', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2015-03-19', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[Constant(value='ValidationError', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2015-03-26', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[Constant(value='ValidationError', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2015-03-25', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='survey_manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_answer_validation_numerical',
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
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_question',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='page_0',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Q0', kind=None),
                                    Constant(value='numerical_box', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='validation_required',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='validation_min_float_value',
                                        value=Constant(value=2.2, kind=None),
                                    ),
                                    keyword(
                                        arg='validation_max_float_value',
                                        value=Constant(value=3.3, kind=None),
                                    ),
                                    keyword(
                                        arg='validation_error_msg',
                                        value=Constant(value='ValidationError', kind=None),
                                    ),
                                ],
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
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Is Alfred an answer ?', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This is not a number', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2.0', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[Constant(value='ValidationError', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='4.0', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[Constant(value='ValidationError', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2.9', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='survey_manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_answer_validation_char_box_email',
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
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_question',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='page_0',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Q0', kind=None),
                                    Constant(value='char_box', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='validation_email',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
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
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='not an email', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This answer must be an email address', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='email@example.com', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='survey_manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_answer_validation_char_box_length',
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
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_question',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='page_0',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Q0', kind=None),
                                    Constant(value='char_box', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='validation_required',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='validation_length_min',
                                        value=Constant(value=2, kind=None),
                                    ),
                                    keyword(
                                        arg='validation_length_max',
                                        value=Constant(value=8, kind=None),
                                    ),
                                    keyword(
                                        arg='validation_error_msg',
                                        value=Constant(value='ValidationError', kind=None),
                                    ),
                                ],
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
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[Constant(value='ValidationError', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='waytoomuchlonganswer', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[Constant(value='ValidationError', kind=None)],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='validate_question',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='valid', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='survey_manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_partial_scores_simple_choice',
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
                            value=Constant(value='" Check that if partial scores are given for partially correct answers, in the case of a multiple\n        choice question with single choice, choosing the answer with max score gives 100% of points. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partial_scores_survey', ctx=Store())],
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
                                            Constant(value='scoring_type', kind=None),
                                            Constant(value='scoring_success_min', kind=None),
                                        ],
                                        values=[
                                            Constant(value='How much do you know about words?', kind=None),
                                            Constant(value='scoring_with_answers', kind=None),
                                            Constant(value=90.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[
                                        Name(id='a_01', ctx=Store()),
                                        Name(id='a_02', ctx=Store()),
                                        Name(id='a_03', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
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
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='answer_score', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A thing full of letters.', kind=None),
                                                    Constant(value=1.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='answer_score', kind=None),
                                                    Constant(value='is_correct', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A unit of language, [...], carrying a meaning.', kind=None),
                                                    Constant(value=4.0, kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='answer_score', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='42', kind=None),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=4.0, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='q_01', ctx=Store())],
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
                                                value=Name(id='partial_scores_survey', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='What is a word?', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='simple_choice', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=BinOp(
                                                                    left=BinOp(
                                                                        left=Name(id='a_01', ctx=Load()),
                                                                        op=BitOr(),
                                                                        right=Name(id='a_02', ctx=Load()),
                                                                    ),
                                                                    op=BitOr(),
                                                                    right=Name(id='a_03', ctx=Load()),
                                                                ),
                                                                attr='ids',
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
                            targets=[Name(id='user_input', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='survey_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='partial_scores_survey', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='user_input_id', kind=None),
                                            Constant(value='question_id', kind=None),
                                            Constant(value='answer_type', kind=None),
                                            Constant(value='suggested_answer_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='user_input', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='q_01', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='suggestion', kind=None),
                                            Attribute(
                                                value=Name(id='a_02', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    Attribute(
                                        value=Name(id='user_input', ctx=Load()),
                                        attr='scoring_percentage',
                                        ctx=Load(),
                                    ),
                                    Constant(value=100, kind=None),
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
                                    Attribute(
                                        value=Name(id='user_input', ctx=Load()),
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
                FunctionDef(
                    name='test_skipped_values',
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
                            value=Constant(value=" Create one question per type of questions.\n        Make sure they are correctly registered as 'skipped' after saving an empty answer for each\n        of them. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='questions', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_one_question_per_type',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='survey_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='survey',
                                        ctx=Load(),
                                    ),
                                    attr='_create_answer',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='user',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='survey_user',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='question', ctx=Store()),
                            iter=Name(id='questions', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='answer', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='question_type',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                List(
                                                    elts=[
                                                        Constant(value='char_box', kind=None),
                                                        Constant(value='text_box', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        body=Constant(value='', kind=None),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey_user', ctx=Load()),
                                            attr='save_lines',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='question', ctx=Load()),
                                            Name(id='answer', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='question', ctx=Store()),
                            iter=Name(id='questions', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_assert_skipped_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='question', ctx=Load()),
                                            Name(id='survey_user', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='survey_manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
