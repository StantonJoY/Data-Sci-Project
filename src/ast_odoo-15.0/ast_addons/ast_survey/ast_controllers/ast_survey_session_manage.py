Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='NotFound', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='http', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='is_html_empty', asname=None)],
            level=0,
        ),
        ClassDef(
            name='UserInputSession',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_fetch_from_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check that given survey_token matches a survey 'access_token'.\n        Unlike the regular survey controller, user trying to access the survey must have full access rights! ", kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.survey', kind=None),
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
                                                    Constant(value='access_token', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='survey_token', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='_fetch_from_session_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Matches a survey against a passed session_code.\n        We don't limit the session_state to be reachable (ready / in_progress) here because\n        in some cases, we want closed session as well (where session_state = False).\n        Instead, when necessary, the reachability is forced in routes calling this method to\n        avoid people using those routes to access other (private) surveys.\n        We limit to sessions opened within the last 7 days to avoid potential abuses. ", kind=None),
                        ),
                        If(
                            test=Name(id='session_code', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='matching_survey', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='survey.survey', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='session_start_time', kind=None),
                                                            Constant(value='>', kind=None),
                                                            BinOp(
                                                                left=Call(
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
                                                                op=Sub(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=Constant(value=7, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='session_code', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='session_code', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='matching_survey', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Name(id='matching_survey', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_session_manage',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Main route used by the host to \'manager\' the session.\n        - If the state of the session is \'ready\'\n          We render a template allowing the host to showcase the different options of the session\n          and to actually start the session.\n          If there are no questions, a "void content" is displayed instead to avoid displaying a\n          blank survey.\n        - If the state of the session is \'in_progress\'\n          We render a template allowing the host to show the question results, display the attendees\n          leaderboard or go to the next question of the session. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='survey_token', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='survey', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='session_state',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='NotFound', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='survey', ctx=Load()),
                                    attr='session_state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ready', kind=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='question_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='survey.survey_void_content', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='survey', kind=None),
                                                            Constant(value='answer', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='survey', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='survey.user_input', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='survey.user_input_session_open', kind=None),
                                            Dict(
                                                keys=[Constant(value='survey', kind=None)],
                                                values=[Name(id='survey', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='template_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_manage_session_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='survey', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='survey.user_input_session_manage', kind=None),
                                            Name(id='template_values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/survey/session/manage/<string:survey_token>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_session_next_question',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='go_back', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" This route is called when the host goes to the next question of the session.\n\n        It's not a regular 'request.render' route because we handle the transition between\n        questions using a AJAX call to be able to display a bioutiful fade in/out effect.\n\n        It triggers the next question of the session.\n\n        We artificially add 1 second to the 'current_question_start_time' to account for server delay.\n        As the timing can influence the attendees score, we try to be fair with everyone by giving them\n        an extra second before we start counting down.\n\n        Frontend should take the delay into account by displaying the appropriate animations.\n\n        Writing the next question on the survey is sudo'ed to avoid potential access right issues.\n        e.g: a survey user can create a live session from any survey but he can only write\n        on its own survey. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='survey_token', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='survey', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='session_state',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='survey', ctx=Load()),
                                    attr='session_state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ready', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='_session_open',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='next_question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey', ctx=Load()),
                                    attr='_get_session_next_question',
                                    ctx=Load(),
                                ),
                                args=[Name(id='go_back', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='next_question', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='now', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='datetime',
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='session_question_id', kind=None),
                                                    Constant(value='session_question_start_time', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='next_question', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Call(
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
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='seconds',
                                                                    value=Constant(value=1, kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='bus.bus', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_sendone',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='access_token',
                                                ctx=Load(),
                                            ),
                                            Constant(value='next_question', kind=None),
                                            Dict(
                                                keys=[Constant(value='question_start', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='now', ctx=Load()),
                                                            attr='timestamp',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='template_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_manage_session_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='survey', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='is_rpc_call', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='survey.user_input_session_manage_content', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/survey/session/next_question/<string:survey_token>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_session_results',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" This route is called when the host shows the current question's results.\n\n        It's not a regular 'request.render' route because we handle the display of results using\n        an AJAX request to be able to include the results in the currently displayed page. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='survey_token', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='survey', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='session_state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='in_progress', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='user_input_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
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
                                            Tuple(
                                                elts=[
                                                    Constant(value='question_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='survey', ctx=Load()),
                                                            attr='session_question_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_date', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Attribute(
                                                        value=Name(id='survey', ctx=Load()),
                                                        attr='session_start_time',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_question_results_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='user_input_lines', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/survey/session/results/<string:survey_token>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_session_leaderboard',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" This route is called when the host shows the current question's attendees leaderboard.\n\n        It's not a regular 'request.render' route because we handle the display of the leaderboard\n        using an AJAX request to be able to include the results in the currently displayed page. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='survey_token', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='survey', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='session_state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='in_progress', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='survey.user_input_session_leaderboard', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='animate', kind=None),
                                            Constant(value='leaderboard', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='_prepare_leaderboard_values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/survey/session/leaderboard/<string:survey_token>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_session_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Renders the survey session code page route.\n        This page allows the user to enter the session code of the survey.\n        It is mainly used to ease survey access for attendees in session mode. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='survey.survey_session_code', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/s', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_start_short',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='" Redirects to \'survey_start\' route using a shortened link & token.\n        We match the session_code for open surveys.\n        This route is used in survey sessions where we need short links for people to type. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_session_code',
                                    ctx=Load(),
                                ),
                                args=[Name(id='session_code', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='survey', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='session_state',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='ready', kind=None),
                                                    Constant(value='in_progress', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='/survey/start/%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='access_token',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/s', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/s/<string:session_code>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_check_session_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Checks if the given code is matching a survey session_code.\n        If yes, redirect to /s/code route.\n        If not, return error. The user is invited to type again the code. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_session_code',
                                    ctx=Load(),
                                ),
                                args=[Name(id='session_code', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='survey', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='session_state',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='ready', kind=None),
                                                    Constant(value='in_progress', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='survey_url', kind=None)],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='/survey/start/%s', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='survey', ctx=Load()),
                                                            attr='access_token',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[Constant(value='survey_session_closed', kind=None)],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='error', kind=None)],
                                values=[Constant(value='survey_wrong', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/survey/check_session_code/<string:session_code>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_manage_session_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='is_first_question', ctx=Store()),
                                        Name(id='is_last_question', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='survey', ctx=Load()),
                                attr='question_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='most_voted_answers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='_get_session_most_voted_answers',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_first_question', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='_is_first_page_or_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='session_question_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_last_question', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='_is_last_page_or_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='most_voted_answers', ctx=Load()),
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='session_question_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='survey', kind=None),
                                    Constant(value='is_last_question', kind=None),
                                    Constant(value='is_first_question', kind=None),
                                ],
                                values=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='is_last_question', ctx=Load()),
                                    Name(id='is_first_question', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_question_results_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='survey', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='survey.user_input.line', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_question_results_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='user_input_lines', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Prepares usefull values to display during the host session:\n\n        - question_statistics_graph\n          The graph data to display the bar chart for questions of type 'choice'\n        - input_lines_values\n          The answer values to text/date/datetime questions\n        - answers_validity\n          An array containing the is_correct value for all question answers.\n          We need this special variable because of Chartjs data structure.\n          The library determines the parameters (color/label/...) by only passing the answer 'index'\n          (and not the id or anything else we can identify).\n          In other words, we need to know if the answer at index 2 is correct or not.\n        - answer_count\n          The number of answers to the current question. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Attribute(
                                value=Name(id='survey', ctx=Load()),
                                attr='session_question_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='answers_validity', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='answer', ctx=Load()),
                                            attr='is_correct',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='answer', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='suggested_answer_ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='answers_validity', ctx=Store())],
                                    value=ListComp(
                                        elt=Attribute(
                                            value=Name(id='answer', ctx=Load()),
                                            attr='is_correct',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='answer', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='suggested_answer_ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='question', ctx=Load()),
                                        attr='comment_count_as_answer',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='answers_validity', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=False, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='full_statistics', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='question', ctx=Load()),
                                        attr='_prepare_statistics',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='user_input_lines', ctx=Load())],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='input_line_values', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
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
                                            Constant(value='date', kind=None),
                                            Constant(value='datetime', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='input_line_values', ctx=Store())],
                                    value=ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='id', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=BinOp(
                                                        left=Constant(value='value_%s', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='question', ctx=Load()),
                                                            attr='question_type',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='line', ctx=Store()),
                                                iter=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='full_statistics', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='table_data', kind=None),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='survey.user_input.line', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=100, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='is_html_empty', kind=None),
                                    Constant(value='question_statistics_graph', kind=None),
                                    Constant(value='input_line_values', kind=None),
                                    Constant(value='answers_validity', kind=None),
                                    Constant(value='answer_count', kind=None),
                                    Constant(value='attendees_count', kind=None),
                                ],
                                values=[
                                    Name(id='is_html_empty', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='full_statistics', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='graph_data', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='input_line_values', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='answers_validity', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='session_question_answer_count',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='session_answer_count',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
