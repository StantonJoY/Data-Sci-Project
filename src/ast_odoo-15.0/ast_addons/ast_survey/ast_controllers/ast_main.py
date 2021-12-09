Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_ui_view',
            names=[alias(name='keep_query', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='request', asname=None),
                alias(name='content_disposition', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='format_datetime', asname=None),
                alias(name='format_date', asname=None),
                alias(name='is_html_empty', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Survey',
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
                    name='_fetch_from_access_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check that given token matches an answer from the given survey_id.\n        Returns a sudo-ed browse record of survey in order to avoid access rights\n        issues now that access is granted through token. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
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
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='answer_token', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='answer_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='survey.user_input', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='answer_sudo', ctx=Store())],
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
                                                        slice=Constant(value='survey.user_input', kind=None),
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
                                                            Constant(value='survey_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='survey_sudo', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='access_token', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='answer_token', ctx=Load()),
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
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='survey_sudo', ctx=Load()),
                                    Name(id='answer_sudo', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_validity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                            arg(arg='ensure_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check survey is open and can be taken. This does not checks for\n        security rules, only functional / business rules. It returns a string key\n        allowing further manipulation of validity issues\n\n         * survey_wrong: survey does not exist;\n         * survey_auth: authentication is required;\n         * survey_closed: survey is closed and does not accept input anymore;\n         * survey_void: survey is void and should not be taken;\n         * token_wrong: given token not recognized;\n         * token_required: no token given although it is necessary to access the\n           survey;\n         * answer_deadline: token linked to an expired answer;\n\n        :param ensure_token: whether user input existence based on given access token\n          should be enforced or not, depending on the route requesting a token or\n          allowing external world calls;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_access_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='survey_sudo', ctx=Load()),
                                        attr='exists',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='survey_wrong', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='answer_token', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='answer_sudo', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='token_wrong', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='answer_sudo', ctx=Load()),
                                    ),
                                    Name(id='ensure_token', ctx=Load()),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='token_required', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='answer_sudo', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='access_mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='token', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='token_required', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='survey_sudo', ctx=Load()),
                                        attr='users_login_required',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='_is_public',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='survey_auth', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='active',
                                            ctx=Load(),
                                        ),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='answer_sudo', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='test_entry',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='survey_closed', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='page_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='questions_layout',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='page_per_section', kind=None)],
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='question_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='survey_void', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='answer_sudo', ctx=Load()),
                                    Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='deadline',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='deadline',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='answer_deadline', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_access_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                            arg(arg='ensure_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get back data related to survey and user input, given the ID and access\n        token provided by the route.\n\n         : param ensure_token: whether user input existence should be enforced or not(see ``_check_validity``)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
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
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='survey.user_input', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='has_survey_access', ctx=Store()),
                                        Name(id='can_answer', ctx=Store()),
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
                        Assign(
                            targets=[Name(id='validity_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_validity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Name(id='ensure_token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='validity_code', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='survey_wrong', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='survey_sudo', ctx=Store()),
                                                Name(id='answer_sudo', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_fetch_from_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='survey_token', ctx=Load()),
                                            Name(id='answer_token', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='survey_user', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
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
                                                    value=Name(id='survey_user', ctx=Load()),
                                                    attr='check_access_rights',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Constant(value='read', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='raise_exception',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='survey_user', ctx=Load()),
                                                    attr='check_access_rule',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Constant(value='read', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=None,
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='has_survey_access', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='can_answer', ctx=Store())],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='answer_sudo', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='can_answer', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='can_answer', ctx=Store())],
                                            value=Compare(
                                                left=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='access_mode',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='public', kind=None)],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='survey_sudo', kind=None),
                                    Constant(value='answer_sudo', kind=None),
                                    Constant(value='has_survey_access', kind=None),
                                    Constant(value='can_answer', kind=None),
                                    Constant(value='validity_code', kind=None),
                                ],
                                values=[
                                    Name(id='survey_sudo', ctx=Load()),
                                    Name(id='answer_sudo', ctx=Load()),
                                    Name(id='has_survey_access', ctx=Load()),
                                    Name(id='can_answer', ctx=Load()),
                                    Name(id='validity_code', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_redirect_with_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='access_data', annotation=None, type_comment=None),
                            arg(arg='error_key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='survey_sudo', ctx=Store())],
                            value=Subscript(
                                value=Name(id='access_data', ctx=Load()),
                                slice=Constant(value='survey_sudo', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='answer_sudo', ctx=Store())],
                            value=Subscript(
                                value=Name(id='access_data', ctx=Load()),
                                slice=Constant(value='answer_sudo', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='error_key', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='survey_void', kind=None)],
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='can_answer', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                                    Name(id='survey_sudo', ctx=Load()),
                                                    Name(id='answer_sudo', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='error_key', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='survey_closed', kind=None)],
                                            ),
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='can_answer', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
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
                                                    Constant(value='survey.survey_closed_expired', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='survey', kind=None)],
                                                        values=[Name(id='survey_sudo', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='error_key', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='survey_auth', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='answer_sudo', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='redirect_url', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='/web/login?redirect=/survey/start/%s', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                                    attr='access_token',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                attr='access_token',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                                attr='partner_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='answer_sudo', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='user_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='survey_sudo', ctx=Load()),
                                                                                        attr='users_can_signup',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='user_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='signup_cancel',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='signup_prepare',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='expiration',
                                                                                                value=BinOp(
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
                                                                                                                arg='days',
                                                                                                                value=Constant(value=1, kind=None),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='redirect_url', ctx=Store())],
                                                                            value=Subscript(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='answer_sudo', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='_get_signup_url_for_action',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[
                                                                                        keyword(
                                                                                            arg='url',
                                                                                            value=BinOp(
                                                                                                left=Constant(value='/survey/start/%s?answer_token=%s', kind=None),
                                                                                                op=Mod(),
                                                                                                right=Tuple(
                                                                                                    elts=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                                                                            attr='access_token',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        Attribute(
                                                                                                            value=Name(id='answer_sudo', ctx=Load()),
                                                                                                            attr='access_token',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                slice=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='answer_sudo', ctx=Load()),
                                                                                        attr='partner_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[Name(id='redirect_url', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Constant(value='/web/login?redirect=%s', kind=None),
                                                                                op=Mod(),
                                                                                right=BinOp(
                                                                                    left=Constant(value='/survey/start/%s?answer_token=%s', kind=None),
                                                                                    op=Mod(),
                                                                                    right=Tuple(
                                                                                        elts=[
                                                                                            Attribute(
                                                                                                value=Name(id='survey_sudo', ctx=Load()),
                                                                                                attr='access_token',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                                                attr='access_token',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='render',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='survey.survey_auth_required', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='survey', kind=None),
                                                                    Constant(value='redirect_url', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='survey_sudo', ctx=Load()),
                                                                    Name(id='redirect_url', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='error_key', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='answer_deadline', kind=None)],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                attr='access_token',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                                    Constant(value='survey.survey_closed_expired', kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='survey', kind=None)],
                                                                        values=[Name(id='survey_sudo', ctx=Load())],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_test',
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
                            value=Constant(value=' Test mode for surveys: create a test answer, only for managers or officers\n        testing their surveys ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fetch_from_access_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='answer_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='_create_answer',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='user',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='test_entry',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/start/%s?%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='access_token',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Name(id='keep_query', ctx=Load()),
                                                    args=[Constant(value='*', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='answer_token',
                                                            value=Attribute(
                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                attr='access_token',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                            args=[Constant(value='/survey/test/<string:survey_token>', kind=None)],
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
                    name='survey_retry',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" This route is called whenever the user has attempts left and hits the 'Retry' button\n        after failing the survey.", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_redirect_with_error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='access_data', ctx=Load()),
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='validity_code', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='answer_sudo', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='retry_answer_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='_create_answer',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='user',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='partner',
                                                value=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='email',
                                                value=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invite_token',
                                                value=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='invite_token',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='test_entry',
                                                value=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='test_entry',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg=None,
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_prepare_retry_additional_values',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='answer_sudo', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/start/%s?%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='access_token',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Name(id='keep_query', ctx=Load()),
                                                    args=[Constant(value='*', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='answer_token',
                                                            value=Attribute(
                                                                value=Name(id='retry_answer_sudo', ctx=Load()),
                                                                attr='access_token',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                            args=[Constant(value='/survey/retry/<string:survey_token>/<string:answer_token>', kind=None)],
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
                    name='_prepare_retry_additional_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[Constant(value='deadline', kind=None)],
                                values=[
                                    Attribute(
                                        value=Name(id='answer', ctx=Load()),
                                        attr='deadline',
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
                FunctionDef(
                    name='_prepare_survey_finished_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='survey', kind=None),
                                    Constant(value='answer', kind=None),
                                ],
                                values=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='answer', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='token', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='token', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='scoring_type',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='no_scoring', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='certification',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='graph_data', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='answer', ctx=Load()),
                                                        attr='_prepare_statistics',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Name(id='answer', ctx=Load()),
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
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_start',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Start a survey by providing\n         * a token linked to a survey;\n         * a token linked to an answer or generate a new token if access is allowed;\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='answer_token', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='answer_token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='cookies',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='survey_%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='survey_token', ctx=Load()),
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
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_redirect_with_error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='access_data', ctx=Load()),
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='validity_code', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='answer_sudo', ctx=Load()),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='answer_sudo', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='_create_answer',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='user',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='email',
                                                        value=Name(id='email', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='UserError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='answer_sudo', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='answer_sudo', ctx=Load()),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='check_access_rights',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='read', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='check_access_rule',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='read', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=None,
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='redirect',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='/', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='survey.survey_403_page', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='survey', kind=None)],
                                                        values=[Name(id='survey_sudo', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    finalbody=[],
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
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='access_token',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='access_token',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                            args=[Constant(value='/survey/start/<string:survey_token>', kind=None)],
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
                    name='_prepare_survey_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_sudo', annotation=None, type_comment=None),
                            arg(arg='answer_sudo', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method prepares all the data needed for template rendering, in function of the survey user input state.\n            :param post:\n                - previous_page_id : come from the breadcrumb or the back button and force the next questions to load\n                                     to be the previous ones. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='is_html_empty', kind=None),
                                    Constant(value='survey', kind=None),
                                    Constant(value='answer', kind=None),
                                    Constant(value='breadcrumb_pages', kind=None),
                                    Constant(value='format_datetime', kind=None),
                                    Constant(value='format_date', kind=None),
                                ],
                                values=[
                                    Name(id='is_html_empty', ctx=Load()),
                                    Name(id='survey_sudo', ctx=Load()),
                                    Name(id='answer_sudo', ctx=Load()),
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='id', kind=None),
                                                Constant(value='title', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='title',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='page', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='page_ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='dt', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Name(id='format_datetime', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                Name(id='dt', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='dt_format',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='date', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Name(id='format_date', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                Name(id='date', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='survey_sudo', ctx=Load()),
                                    attr='questions_layout',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='page_per_question', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='triggering_answer_by_question', ctx=Store()),
                                                Name(id='triggered_questions_by_answer', ctx=Store()),
                                                Name(id='selected_answers', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='_get_conditional_values',
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
                                            value=Name(id='data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='triggering_answer_by_question', kind=None),
                                                    Constant(value='triggered_questions_by_answer', kind=None),
                                                    Constant(value='selected_answers', kind=None),
                                                ],
                                                values=[
                                                    DictComp(
                                                        key=Attribute(
                                                            value=Name(id='question', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='triggering_answer_by_question', ctx=Load()),
                                                                slice=Name(id='question', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='question', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='triggering_answer_by_question', ctx=Load()),
                                                                        attr='keys',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[
                                                                    Subscript(
                                                                        value=Name(id='triggering_answer_by_question', ctx=Load()),
                                                                        slice=Name(id='question', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    DictComp(
                                                        key=Attribute(
                                                            value=Name(id='answer', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='triggered_questions_by_answer', ctx=Load()),
                                                                slice=Name(id='answer', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='answer', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='triggered_questions_by_answer', ctx=Load()),
                                                                        attr='keys',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='selected_answers', ctx=Load()),
                                                        attr='ids',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='is_session_answer',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='survey_sudo', ctx=Load()),
                                        attr='is_time_limited',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='start_datetime',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='server_time', kind=None),
                                                    Constant(value='timer_start', kind=None),
                                                    Constant(value='time_limit_minutes', kind=None),
                                                ],
                                                values=[
                                                    Call(
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
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                attr='start_datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='isoformat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='survey_sudo', ctx=Load()),
                                                        attr='time_limit',
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
                        Assign(
                            targets=[Name(id='page_or_question_key', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Name(id='survey_sudo', ctx=Load()),
                                        attr='questions_layout',
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='page_per_question', kind=None)],
                                ),
                                body=Constant(value='question', kind=None),
                                orelse=Constant(value='page', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='previous_page_id', kind=None),
                                ops=[In()],
                                comparators=[Name(id='post', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='previous_page_or_question_id', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='post', ctx=Load()),
                                                slice=Constant(value='previous_page_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_previous_id', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='survey_sudo', ctx=Load()),
                                                attr='_get_next_page_or_question',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='answer_sudo', ctx=Load()),
                                                Name(id='previous_page_or_question_id', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='go_back',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='page_or_question', ctx=Store())],
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
                                                        slice=Constant(value='survey.question', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='previous_page_or_question_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Name(id='page_or_question_key', ctx=Load()),
                                                    Constant(value='previous_page_id', kind=None),
                                                    Constant(value='has_answered', kind=None),
                                                    Constant(value='can_go_back', kind=None),
                                                ],
                                                values=[
                                                    Name(id='page_or_question', ctx=Load()),
                                                    Name(id='new_previous_id', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                attr='user_input_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='question_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='new_previous_id', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                            attr='_can_go_back',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='answer_sudo', ctx=Load()),
                                                            Name(id='page_or_question', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='data', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='answer_sudo', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='in_progress', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='is_session_answer',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='next_page_or_question', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='survey_sudo', ctx=Load()),
                                                attr='session_question_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='next_page_or_question', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='_get_next_page_or_question',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='answer_sudo', ctx=Load()),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Name(id='answer_sudo', ctx=Load()),
                                                            attr='last_displayed_page_id',
                                                            ctx=Load(),
                                                        ),
                                                        body=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                attr='last_displayed_page_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=0, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='next_page_or_question', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='data', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='survey_last', kind=None)],
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                                            attr='_is_last_page_or_question',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='answer_sudo', ctx=Load()),
                                                                            Name(id='next_page_or_question', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
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
                                    ],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='answer_sudo', ctx=Load()),
                                                attr='is_session_answer',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='next_page_or_question', ctx=Load()),
                                                attr='is_time_limited',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='timer_start', kind=None),
                                                            Constant(value='time_limit_minutes', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='survey_sudo', ctx=Load()),
                                                                        attr='session_question_start_time',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='isoformat',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='next_page_or_question', ctx=Load()),
                                                                    attr='time_limit',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Div(),
                                                                right=Constant(value=60, kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Name(id='page_or_question_key', ctx=Load()),
                                                    Constant(value='has_answered', kind=None),
                                                    Constant(value='can_go_back', kind=None),
                                                ],
                                                values=[
                                                    Name(id='next_page_or_question', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='answer_sudo', ctx=Load()),
                                                                attr='user_input_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='question_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='next_page_or_question', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                            attr='_can_go_back',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='answer_sudo', ctx=Load()),
                                                            Name(id='next_page_or_question', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='questions_layout',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='one_page', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='previous_page_id', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='survey_sudo', ctx=Load()),
                                                                        attr='_get_next_page_or_question',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Name(id='answer_sudo', ctx=Load()),
                                                                        Attribute(
                                                                            value=Name(id='next_page_or_question', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='go_back',
                                                                            value=Constant(value=True, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                                attr='id',
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
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='done', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='answer_sudo', ctx=Load()),
                                                attr='survey_time_limit_reached',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_survey_finished_values',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='survey_sudo', ctx=Load()),
                                                    Name(id='answer_sudo', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_question_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_sudo', annotation=None, type_comment=None),
                            arg(arg='answer_sudo', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Survey page navigation is done in AJAX. This function prepare the 'next page' to display in html\n        and send back this html to the survey_form widget that will inject it into the page.", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_survey_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_sudo', ctx=Load()),
                                    Name(id='answer_sudo', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='survey_content', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='answer_sudo', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='done', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='survey_content', ctx=Store())],
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
                                                args=[Constant(value='survey.survey_fill_form_done', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='survey_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='survey_content', ctx=Store())],
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
                                                args=[Constant(value='survey.survey_fill_form_in_progress', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='survey_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='survey_progress', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='in_progress', kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='survey_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='question', kind=None),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='survey.question', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='is_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='questions_layout',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='page_per_section', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='page_ids', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='page_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='survey_progress', ctx=Store())],
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
                                                        args=[Constant(value='survey.survey_progression', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='survey', kind=None),
                                                            Constant(value='page_ids', kind=None),
                                                            Constant(value='page_number', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='survey_sudo', ctx=Load()),
                                                            Name(id='page_ids', ctx=Load()),
                                                            BinOp(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='page_ids', ctx=Load()),
                                                                        attr='index',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='survey_data', ctx=Load()),
                                                                                slice=Constant(value='page', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=IfExp(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                                            attr='progression_mode',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='number', kind=None)],
                                                                    ),
                                                                    body=Constant(value=1, kind=None),
                                                                    orelse=Constant(value=0, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='questions_layout',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='page_per_question', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='page_ids', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                            attr='question_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='survey_progress', ctx=Store())],
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
                                                                args=[Constant(value='survey.survey_progression', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='_render',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='survey', kind=None),
                                                                    Constant(value='page_ids', kind=None),
                                                                    Constant(value='page_number', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='survey_sudo', ctx=Load()),
                                                                    Name(id='page_ids', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='page_ids', ctx=Load()),
                                                                            attr='index',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='survey_data', ctx=Load()),
                                                                                    slice=Constant(value='question', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='survey_content', kind=None),
                                    Constant(value='survey_progress', kind=None),
                                    Constant(value='survey_navigation', kind=None),
                                ],
                                values=[
                                    Name(id='survey_content', ctx=Load()),
                                    Name(id='survey_progress', ctx=Load()),
                                    Call(
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
                                                args=[Constant(value='survey.survey_navigation', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='survey_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_display_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_redirect_with_error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='access_data', ctx=Load()),
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='validity_code', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='answer_sudo', ctx=Store())],
                            value=Subscript(
                                value=Name(id='access_data', ctx=Load()),
                                slice=Constant(value='answer_sudo', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='done', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='survey_time_limit_reached',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='_mark_done',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                    Constant(value='survey.survey_page_fill', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_survey_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='survey_sudo', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='answer_sudo', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='post', ctx=Load()),
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
                            args=[Constant(value='/survey/<string:survey_token>/<string:answer_token>', kind=None)],
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
                    name='survey_get_background',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='Forbidden',
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='image_base64', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='ir.http', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='survey.survey', kind=None),
                                    ),
                                    keyword(
                                        arg='id',
                                        value=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Constant(value='background_image', kind=None),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='image/png', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_content_image_get_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Name(id='headers', ctx=Load()),
                                    Name(id='image_base64', ctx=Load()),
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
                            args=[Constant(value='/survey/get_background_image/<string:survey_token>/<string:answer_token>', kind=None)],
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
                    name='survey_get_question_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                            arg(arg='question_id', annotation=None, type_comment=None),
                            arg(arg='suggested_answer_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='Forbidden',
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='survey_sudo', ctx=Load()),
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
                                                args=[arg(arg='a', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Compare(
                                                left=Attribute(
                                                    value=Name(id='a', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='suggested_answer_id', ctx=Load())],
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='image_base64', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='ir.http', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='survey.question.answer', kind=None),
                                    ),
                                    keyword(
                                        arg='id',
                                        value=Name(id='suggested_answer_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Constant(value='value_image', kind=None),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='image/png', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_content_image_get_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Name(id='headers', ctx=Load()),
                                    Name(id='image_base64', ctx=Load()),
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
                            args=[Constant(value='/survey/get_question_image/<string:survey_token>/<string:answer_token>/<int:question_id>/<int:suggested_answer_id>', kind=None)],
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
                    name='survey_begin',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Route used to start the survey user input and display the first survey page. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='validity_code', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='answer_sudo', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='new', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The survey has already started.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='answer_sudo', ctx=Load()),
                                    attr='_mark_in_progress',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_question_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_sudo', ctx=Load()),
                                    Name(id='answer_sudo', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
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
                            args=[Constant(value='/survey/begin/<string:survey_token>/<string:answer_token>', kind=None)],
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
                    name='survey_next_question',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Method used to display the next survey question in an ongoing session.\n        Triggered on all attendees screens when the host goes to the next question. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='validity_code', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='new', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='is_session_answer',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='_mark_in_progress',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_question_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_sudo', ctx=Load()),
                                    Name(id='answer_sudo', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
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
                            args=[Constant(value='/survey/next_question/<string:survey_token>/<string:answer_token>', kind=None)],
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
                    name='survey_submit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Submit a page from the survey.\n        This will take into account the validation errors and store the answers to the questions.\n        If the time limit is reached, errors will be skipped, answers will be ignored and\n        survey state will be forced to 'done'", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='access_data', ctx=Load()),
                                    slice=Constant(value='validity_code', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='validity_code', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='answer_sudo', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='done', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='unauthorized', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='questions', ctx=Store()),
                                        Name(id='page_or_question_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey_sudo', ctx=Load()),
                                    attr='_get_survey_questions',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='answer',
                                        value=Name(id='answer_sudo', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='page_id',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='page_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='question_id',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='question_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='test_entry',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='survey_sudo', ctx=Load()),
                                                attr='_has_attempts_left',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='invite_token',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='unauthorized', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='survey_time_limit_reached',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='question_time_limit_reached',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='question_time_limit_reached',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='time_limit', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                    attr='session_question_start_time',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='seconds',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='survey_sudo', ctx=Load()),
                                                                    attr='session_question_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='time_limit',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='time_limit', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='timedelta', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='seconds',
                                                        value=Constant(value=3, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='time_limit', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='start_datetime',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='minutes',
                                                            value=Attribute(
                                                                value=Name(id='survey_sudo', ctx=Load()),
                                                                attr='time_limit',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='time_limit', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='timedelta', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='seconds',
                                                        value=Constant(value=10, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
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
                                        ops=[Gt()],
                                        comparators=[Name(id='time_limit', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[Constant(value='unauthorized', kind=None)],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='errors', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='question', ctx=Store()),
                            iter=Name(id='questions', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='inactive_questions', ctx=Store())],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='is_session_answer',
                                            ctx=Load(),
                                        ),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='survey.question', kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Call(
                                            func=Attribute(
                                                value=Name(id='answer_sudo', ctx=Load()),
                                                attr='_get_inactive_conditional_questions',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='question', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='inactive_questions', ctx=Load())],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='answer', ctx=Store()),
                                                Name(id='comment', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_extract_comment_from_answers',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='question', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='question', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='validate_question',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='answer', ctx=Load()),
                                                    Name(id='comment', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='errors', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='save_lines',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='question', ctx=Load()),
                                                    Name(id='answer', ctx=Load()),
                                                    Name(id='comment', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='errors', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='survey_time_limit_reached',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='question_time_limit_reached',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='fields', kind=None),
                                        ],
                                        values=[
                                            Constant(value='validation', kind=None),
                                            Name(id='errors', ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='answer_sudo', ctx=Load()),
                                    attr='is_session_answer',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='_clear_inactive_conditional_answers',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='answer_sudo', ctx=Load()),
                                        attr='survey_time_limit_reached',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='survey_sudo', ctx=Load()),
                                            attr='questions_layout',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='one_page', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='answer_sudo', ctx=Load()),
                                            attr='_mark_done',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='previous_page_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='post', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_question_html',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='survey_sudo', ctx=Load()),
                                                    Name(id='answer_sudo', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='post', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='vals', ctx=Store())],
                                            value=Dict(
                                                keys=[Constant(value='last_displayed_page_id', kind=None)],
                                                values=[Name(id='page_or_question_id', ctx=Load())],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='is_session_answer',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='next_page', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                            attr='_get_next_page_or_question',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='answer_sudo', ctx=Load()),
                                                            Name(id='page_or_question_id', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='next_page', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                                    attr='_mark_done',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='vals', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_question_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_sudo', ctx=Load()),
                                    Name(id='answer_sudo', ctx=Load()),
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
                            args=[Constant(value='/survey/submit/<string:survey_token>/<string:answer_token>', kind=None)],
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
                    name='_extract_comment_from_answers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                            arg(arg='answers', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Answers is a custom structure depending of the question type\n        that can contain question answers but also comments that need to be\n        extracted before validating and saving answers.\n        If multiple answers, they are listed in an array, except for matrix\n        where answers are structured differently. See input and output for\n        more info on data structures.\n        :param question: survey.question\n        :param answers:\n          * question_type: free_text, text_box, numerical_box, date, datetime\n            answers is a string containing the value\n          * question_type: simple_choice with no comment\n            answers is a string containing the value ('question_id_1')\n          * question_type: simple_choice with comment\n            ['question_id_1', {'comment': str}]\n          * question_type: multiple choice\n            ['question_id_1', 'question_id_2'] + [{'comment': str}] if holds a comment\n          * question_type: matrix\n            {'matrix_row_id_1': ['question_id_1', 'question_id_2'],\n             'matrix_row_id_2': ['question_id_1', 'question_id_2']\n            } + {'comment': str} if holds a comment\n        :return: tuple(\n          same structure without comment,\n          extracted comment for given question\n        ) ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='comment', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='answers_no_comment', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='answers', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='question_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='matrix', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='comment', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='answers', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='comment', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='answers', ctx=Load()),
                                                                slice=Constant(value='comment', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='strip',
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
                                                            value=Name(id='answers', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='comment', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='answers_no_comment', ctx=Store())],
                                            value=Name(id='answers', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='answers', ctx=Load()),
                                                        Name(id='list', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='answers', ctx=Store())],
                                                    value=List(
                                                        elts=[Name(id='answers', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='answer', ctx=Store()),
                                            iter=Name(id='answers', ctx=Load()),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='answer', ctx=Load()),
                                                                    Name(id='dict', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Compare(
                                                                left=Constant(value='comment', kind=None),
                                                                ops=[In()],
                                                                comparators=[Name(id='answer', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='comment', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='answer', ctx=Load()),
                                                                        slice=Constant(value='comment', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strip',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='answers_no_comment', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='answer', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='answers_no_comment', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='answers_no_comment', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='answers_no_comment', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='answers_no_comment', ctx=Load()),
                                    Name(id='comment', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='survey_print',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_token', annotation=None, type_comment=None),
                            arg(arg='review', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Display an survey in printable view; if <answer_token> is set, it will\n        grab the answers of the user_input_id that has <answer_token>.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='access_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey_token', ctx=Load()),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='ensure_token',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='access_data', ctx=Load()),
                                            slice=Constant(value='validity_code', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=True, kind=None)],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='has_survey_access', kind=None),
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='access_data', ctx=Load()),
                                                    slice=Constant(value='validity_code', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='token_required', kind=None),
                                                            Constant(value='survey_closed', kind=None),
                                                            Constant(value='survey_void', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_redirect_with_error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='access_data', ctx=Load()),
                                            Subscript(
                                                value=Name(id='access_data', ctx=Load()),
                                                slice=Constant(value='validity_code', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='survey_sudo', ctx=Store()),
                                        Name(id='answer_sudo', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='survey_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='access_data', ctx=Load()),
                                        slice=Constant(value='answer_sudo', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                                    Constant(value='survey.survey_page_print', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='is_html_empty', kind=None),
                                            Constant(value='review', kind=None),
                                            Constant(value='survey', kind=None),
                                            Constant(value='answer', kind=None),
                                            Constant(value='questions_to_display', kind=None),
                                            Constant(value='scoring_display_correction', kind=None),
                                            Constant(value='format_datetime', kind=None),
                                            Constant(value='format_date', kind=None),
                                        ],
                                        values=[
                                            Name(id='is_html_empty', ctx=Load()),
                                            Name(id='review', ctx=Load()),
                                            Name(id='survey_sudo', ctx=Load()),
                                            IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='survey_sudo', ctx=Load()),
                                                        attr='scoring_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='scoring_without_answers', kind=None)],
                                                ),
                                                body=Name(id='answer_sudo', ctx=Load()),
                                                orelse=Call(
                                                    func=Attribute(
                                                        value=Name(id='answer_sudo', ctx=Load()),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='answer_sudo', ctx=Load()),
                                                    attr='_get_print_questions',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='survey_sudo', ctx=Load()),
                                                            attr='scoring_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='scoring_with_answers', kind=None)],
                                                    ),
                                                    Name(id='answer_sudo', ctx=Load()),
                                                ],
                                            ),
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='dt', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Call(
                                                    func=Name(id='format_datetime', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='dt', ctx=Load()),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='dt_format',
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='date', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Call(
                                                    func=Name(id='format_date', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='date', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
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
                            args=[Constant(value='/survey/print/<string:survey_token>', kind=None)],
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
                    name='show_certification_pdf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='preview_url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='/survey/%s/get_certification_preview', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='survey', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
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
                                    Constant(value='survey.certification_preview', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='preview_url', kind=None),
                                            Constant(value='page_title', kind=None),
                                        ],
                                        values=[
                                            Name(id='preview_url', ctx=Load()),
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='title',
                                                ctx=Load(),
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
                            args=[Constant(value='/survey/<model("survey.survey"):survey>/certification_preview', kind=None)],
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
                    name='survey_get_certification_preview',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='survey.group_survey_user', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='Forbidden',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='fake_user_input', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey', ctx=Load()),
                                    attr='_create_answer',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='user',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='test_entry',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_report',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fake_user_input', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='download',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fake_user_input', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/survey/<model("survey.survey"):survey>/get_certification_preview', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
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
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
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
                    name='survey_get_certification',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' The certification document can be downloaded as long as the user has succeeded the certification ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='survey', ctx=Store())],
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
                                                    Constant(value='id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='survey_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='certification', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='survey', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='succeeded_attempt', ctx=Store())],
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
                                                slice=Constant(value='survey.user_input', kind=None),
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
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
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
                                                    Constant(value='survey_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='survey_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='scoring_success', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='succeeded_attempt', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The user has not succeeded the certification', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_report',
                                    ctx=Load(),
                                ),
                                args=[Name(id='succeeded_attempt', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='download',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/survey/<int:survey_id>/get_certification', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
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
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
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
                    name='survey_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Display survey Results & Statistics for given survey.\n\n        New structure: {\n            'survey': current survey browse record,\n            'question_and_page_data': see ``SurveyQuestion._prepare_statistics()``,\n            'survey_data'= see ``SurveySurvey._prepare_statistics()``\n            'search_filters': [],\n            'search_finished': either filter on finished inputs only or not,\n        }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='user_input_lines', ctx=Store()),
                                        Name(id='search_filters', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_extract_filters_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='post', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='survey_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='survey', ctx=Load()),
                                    attr='_prepare_statistics',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_input_lines', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='question_and_page_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='question_and_page_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_prepare_statistics',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_input_lines', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='template_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='survey', kind=None),
                                    Constant(value='question_and_page_data', kind=None),
                                    Constant(value='survey_data', kind=None),
                                    Constant(value='search_filters', kind=None),
                                    Constant(value='search_finished', kind=None),
                                ],
                                values=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='question_and_page_data', ctx=Load()),
                                    Name(id='survey_data', ctx=Load()),
                                    Name(id='search_filters', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='post', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='finished', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='true', kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='survey', ctx=Load()),
                                attr='session_show_leaderboard',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='leaderboard', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='_prepare_leaderboard_values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                                    Constant(value='survey.survey_page_statistics', kind=None),
                                    Name(id='template_values', ctx=Load()),
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
                            args=[Constant(value='/survey/results/<model("survey.survey"):survey>', kind=None)],
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
                    name='_generate_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user_input', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='report', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
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
                                                    args=[Constant(value='survey.certification_report', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_render_qweb_pdf',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='user_input', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='data',
                                            value=Dict(
                                                keys=[Constant(value='report_type', kind=None)],
                                                values=[Constant(value='pdf', kind=None)],
                                            ),
                                        ),
                                    ],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_content_disposition', ctx=Store())],
                            value=Call(
                                func=Name(id='content_disposition', ctx=Load()),
                                args=[Constant(value='Certification.pdf', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='download', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='content_split', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='report_content_disposition', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=';', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='content_split', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='inline', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='report_content_disposition', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=';', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='content_split', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[Name(id='report', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Type', kind=None),
                                                        Constant(value='application/pdf', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Length', kind=None),
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='report', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Disposition', kind=None),
                                                        Name(id='report_content_disposition', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
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
                FunctionDef(
                    name='_get_user_input_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='line_filter_domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user_input_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='&', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='test_entry', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
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
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='line_filter_domain', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='matching_line_ids', ctx=Store())],
                                    value=Attribute(
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
                                                            slice=Constant(value='survey.user_input.line', kind=None),
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
                                            args=[Name(id='line_filter_domain', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='user_input_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_input_line_ids', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='matching_line_ids', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='user_input_domain', ctx=Load()),
                                                ],
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='finished', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='user_input_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='done', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='user_input_domain', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='user_input_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='!=', kind=None),
                                                                    Constant(value='new', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='user_input_domain', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='user_input_domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_extract_filters_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='search_filters', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='line_filter_domain', ctx=Store()),
                                        Name(id='line_choices', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    List(elts=[], ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='data', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='post', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='filters', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='|', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='row_id', ctx=Store()),
                                                        Name(id='answer_id', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=GeneratorExp(
                                                elt=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='item', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='item', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='data', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=None,
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='row_id', ctx=Load()),
                                                    Name(id='answer_id', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='line_filter_domain', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='expression', ctx=Load()),
                                                            attr='AND',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='&', kind=None),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='matrix_row_id', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Name(id='row_id', ctx=Load()),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='suggested_answer_id', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Name(id='answer_id', ctx=Load()),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='line_filter_domain', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='answers', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='survey.question.answer', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Name(id='row_id', ctx=Load()),
                                                                    Name(id='answer_id', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='answer_id', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line_choices', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='answer_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='answers', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='survey.question.answer', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='browse',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='answer_id', ctx=Load())],
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
                                            ],
                                        ),
                                        If(
                                            test=Name(id='answer_id', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='question_id', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='answers', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='matrix_question_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='answers', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='question_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='search_filters', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='question', kind=None),
                                                                    Constant(value='answers', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='question_id', ctx=Load()),
                                                                        attr='title',
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Constant(value='%s%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='answers', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='value',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                IfExp(
                                                                                    test=Compare(
                                                                                        left=Call(
                                                                                            func=Name(id='len', ctx=Load()),
                                                                                            args=[Name(id='answers', ctx=Load())],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        ops=[Gt()],
                                                                                        comparators=[Constant(value=1, kind=None)],
                                                                                    ),
                                                                                    body=BinOp(
                                                                                        left=Constant(value=': %s', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Attribute(
                                                                                            value=Subscript(
                                                                                                value=Name(id='answers', ctx=Load()),
                                                                                                slice=Constant(value=1, kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='value',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    orelse=Constant(value='', kind=None),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
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
                                    ],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='line_choices', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='line_filter_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='suggested_answer_id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='line_choices', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='line_filter_domain', ctx=Load()),
                                                ],
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
                            targets=[Name(id='user_input_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_user_input_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='survey', ctx=Load()),
                                    Name(id='line_filter_domain', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_input_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='survey.user_input', kind=None),
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
                                        args=[Name(id='user_input_domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='user_input_line_ids', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='user_input_lines', ctx=Load()),
                                    Name(id='search_filters', ctx=Load()),
                                ],
                                ctx=Load(),
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
