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
            name='TestSurveyFlow',
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
                    name='_format_submission_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='answer_data', annotation=None, type_comment=None),
                            arg(arg='additional_post_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='post_data', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='post_data', ctx=Load()),
                                    slice=Constant(value='page_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='page', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='question_id', ctx=Store()),
                                    Name(id='answer_vals', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='answer_data', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='question', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='question_ids',
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
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='q', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='question_id', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='post_data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_post_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='question', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='answer_vals', ctx=Load()),
                                                        slice=Constant(value='value', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='post_data', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post_data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='additional_post_data', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='post_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_flow_public',
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
                                        args=[Constant(value='survey_manager', kind=None)],
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
                                                    Constant(value='users_login_required', kind=None),
                                                    Constant(value='questions_layout', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Public Survey for Tarte Al Djotte', kind=None),
                                                    Constant(value='public', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='page_per_section', kind=None),
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
                                                    Constant(value='is_page', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='title', kind=None),
                                                    Constant(value='survey_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Page1: Your Data', kind=None),
                                                    Attribute(
                                                        value=Name(id='survey', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='page0_q0', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='What is your name', kind=None),
                                            Constant(value='text_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='comments_allowed',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please enter your name', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page0_q1', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_0', ctx=Load()),
                                            Constant(value='What is your age', kind=None),
                                            Constant(value='numerical_box', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='comments_allowed',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_mandatory',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='constr_error_msg',
                                                value=Constant(value='Please enter your name', kind=None),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page_1', ctx=Store())],
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
                                                    Constant(value='is_page', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='title', kind=None),
                                                    Constant(value='survey_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value='Page2: Tarte Al Djotte', kind=None),
                                                    Attribute(
                                                        value=Name(id='survey', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='page1_q0', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='page_1', ctx=Load()),
                                            Constant(value='What do you like most in our tarte al djotte', kind=None),
                                            Constant(value='multiple_choice', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='labels',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='The gras', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='The bette', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='The tout', kind=None)],
                                                        ),
                                                        Dict(
                                                            keys=[Constant(value='value', kind=None)],
                                                            values=[Constant(value='The regime is fucked up', kind=None)],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='survey_id',
                                                value=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='id',
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
                        Assign(
                            targets=[Name(id='answers', ctx=Store())],
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
                        Assign(
                            targets=[Name(id='answer_lines', ctx=Store())],
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
                                    Name(id='answers', ctx=Load()),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input', kind=None),
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
                                    Name(id='answer_lines', ctx=Load()),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input.line', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_start',
                                    ctx=Load(),
                                ),
                                args=[Name(id='survey', ctx=Load())],
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
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='title',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='answers', ctx=Store())],
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
                                        args=[Name(id='answers', ctx=Load())],
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
                                value=Name(id='answers', ctx=Load()),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[Name(id='answer_token', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAnswer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='answers', ctx=Load()),
                                    Constant(value='new', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
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
                                    Name(id='r', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAnswer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='answers', ctx=Load()),
                                    Constant(value='new', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
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
                                        value=Name(id='r', ctx=Load()),
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
                            targets=[Name(id='answer_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Attribute(
                                        value=Name(id='page0_q0', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='page0_q1', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                values=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[
                                            List(
                                                elts=[Constant(value='Alfred Poilvache', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[
                                            List(
                                                elts=[Constant(value='44.0', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='post_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_submission_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page_0', ctx=Load()),
                                    Name(id='answer_data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='csrf_token', kind=None),
                                            Constant(value='token', kind=None),
                                            Constant(value='button_submit', kind=None),
                                        ],
                                        values=[
                                            Name(id='csrf_token', ctx=Load()),
                                            Name(id='answer_token', ctx=Load()),
                                            Constant(value='next', kind=None),
                                        ],
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
                                    attr='_access_submit',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                    Name(id='post_data', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='answers', ctx=Load()),
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
                                    attr='assertAnswer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='answers', ctx=Load()),
                                    Constant(value='in_progress', kind=None),
                                    Name(id='page_0', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAnswerLines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page_0', ctx=Load()),
                                    Name(id='answers', ctx=Load()),
                                    Name(id='answer_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
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
                                    Name(id='r', ctx=Load()),
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
                                        value=Name(id='r', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='answer_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Attribute(
                                        value=Name(id='page1_q0', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                values=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='page1_q0', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='page1_q0', ctx=Load()),
                                                                attr='suggested_answer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='post_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_submission_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page_1', ctx=Load()),
                                    Name(id='answer_data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='csrf_token', kind=None),
                                            Constant(value='token', kind=None),
                                            Constant(value='button_submit', kind=None),
                                        ],
                                        values=[
                                            Name(id='csrf_token', ctx=Load()),
                                            Name(id='answer_token', ctx=Load()),
                                            Constant(value='next', kind=None),
                                        ],
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
                                    attr='_access_submit',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                    Name(id='post_data', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='answers', ctx=Load()),
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
                                    attr='assertAnswer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='answers', ctx=Load()),
                                    Constant(value='done', kind=None),
                                    Name(id='page_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAnswerLines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page_1', ctx=Load()),
                                    Name(id='answers', ctx=Load()),
                                    Name(id='answer_data', ctx=Load()),
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
