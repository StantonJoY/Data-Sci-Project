Module(
    body=[
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='exceptions', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests.common',
            names=[alias(name='MailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.phone_validation.tools',
            names=[alias(name='phone_validation', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sms.models.sms_api',
            names=[alias(name='SmsApi', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sms.models.sms_sms',
            names=[alias(name='SmsSms', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MockSMS',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='BaseCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='tearDown',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MockSMS', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='tearDown',
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
                                    attr='_clear_sms_sent',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='mockSMSGateway',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sms_allow_unlink', annotation=None, type_comment=None),
                            arg(arg='sim_error', annotation=None, type_comment=None),
                            arg(arg='nbr_t_error', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_clear_sms_sent',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sms_create_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='SmsSms', ctx=Load()),
                                attr='create',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sms_send_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='SmsSms', ctx=Load()),
                                attr='_send',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_contact_iap',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='local_endpoint', annotation=None, type_comment=None),
                                    arg(arg='params', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='local_endpoint', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='/iap/message_send', kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sms',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=ListComp(
                                                elt=Dict(
                                                    keys=[
                                                        Constant(value='number', kind=None),
                                                        Constant(value='body', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='number', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='params', ctx=Load()),
                                                            slice=Constant(value='message', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='number', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Name(id='params', ctx=Load()),
                                                            slice=Constant(value='numbers', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='local_endpoint', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='/iap/sms/2/send', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='to_send', ctx=Store()),
                                            iter=Subscript(
                                                value=Name(id='params', ctx=Load()),
                                                slice=Constant(value='messages', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='credit', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='to_send', ctx=Load()),
                                                                slice=Constant(value='res_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='success', kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='error', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='sim_error', ctx=Load()),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='nbr_t_error', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='nbr_t_error', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='to_send', ctx=Load()),
                                                                                slice=Constant(value='number', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='error', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='error', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='credit', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='credit',
                                                                        value=Constant(value=0, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='state',
                                                                        value=Constant(value='insufficient_credit', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='error', ctx=Load()),
                                                                    Compare(
                                                                        left=Name(id='error', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='wrong_number_format', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            attr='update',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='state',
                                                                                value=Constant(value='wrong_number_format', kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='error', ctx=Load()),
                                                                            Compare(
                                                                                left=Name(id='error', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='unregistered', kind=None)],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='res', ctx=Load()),
                                                                                    attr='update',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='state',
                                                                                        value=Constant(value='unregistered', kind=None),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Name(id='error', ctx=Load()),
                                                                                    Compare(
                                                                                        left=Name(id='error', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='server_error', kind=None)],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='res', ctx=Load()),
                                                                                            attr='update',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='state',
                                                                                                value=Constant(value='server_error', kind=None),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='error', ctx=Load()),
                                                                                            Compare(
                                                                                                left=Name(id='error', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='jsonrpc_exception', kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Raise(
                                                                                            exc=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='exceptions', ctx=Load()),
                                                                                                    attr='AccessError',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    BinOp(
                                                                                                        left=Constant(value='The url that this service requested returned an error. Please contact the author of the app. The url it tried to contact was ', kind=None),
                                                                                                        op=Add(),
                                                                                                        right=Name(id='local_endpoint', ctx=Load()),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            cause=None,
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
                                                    ],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='result', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='res', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Constant(value='state', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='success', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_sms',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='number', kind=None),
                                                                            Constant(value='body', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Subscript(
                                                                                value=Name(id='to_send', ctx=Load()),
                                                                                slice=Constant(value='number', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Subscript(
                                                                                value=Name(id='to_send', ctx=Load()),
                                                                                slice=Constant(value='content', kind=None),
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
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='result', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_sms_sms_create',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sms_create_origin', ctx=Load()),
                                        args=[
                                            Name(id='model', ctx=Load()),
                                            Starred(
                                                value=Name(id='args', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_new_sms',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_sms_sms_send',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='records', annotation=None, type_comment=None),
                                    arg(arg='unlink_failed', annotation=None, type_comment=None),
                                    arg(arg='unlink_sent', annotation=None, type_comment=None),
                                    arg(arg='raise_exception', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=False, kind=None),
                                    Constant(value=True, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            body=[
                                If(
                                    test=Name(id='sms_allow_unlink', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='sms_send_origin', ctx=Load()),
                                                args=[Name(id='records', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='unlink_failed',
                                                        value=Name(id='unlink_failed', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='unlink_sent',
                                                        value=Name(id='unlink_sent', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='raise_exception',
                                                        value=Name(id='raise_exception', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Name(id='sms_send_origin', ctx=Load()),
                                                args=[Name(id='records', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='unlink_failed',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='unlink_sent',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='raise_exception',
                                                        value=Name(id='raise_exception', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='patch', ctx=Load()),
                                                    attr='object',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='SmsApi', ctx=Load()),
                                                    Constant(value='_contact_iap', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='side_effect',
                                                        value=Name(id='_contact_iap', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='patch', ctx=Load()),
                                                    attr='object',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='SmsSms', ctx=Load()),
                                                    Constant(value='create', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='autospec',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='wraps',
                                                        value=Name(id='SmsSms', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='side_effect',
                                                        value=Name(id='_sms_sms_create', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='patch', ctx=Load()),
                                                    attr='object',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='SmsSms', ctx=Load()),
                                                    Constant(value='_send', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='autospec',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='wraps',
                                                        value=Name(id='SmsSms', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='side_effect',
                                                        value=Name(id='_sms_sms_send', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Yield(value=None),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[Pass()],
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_clear_sms_sent',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sms',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_new_sms',
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
                                        slice=Constant(value='sms.sms', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_clear_outoing_sms',
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
                            value=Constant(value=' As SMS gateway mock keeps SMS, we may need to remove them manually\n        if there are several tests in the same tx. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='sms.sms', kind=None),
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
                                                            Constant(value='state', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='outgoing', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
        ClassDef(
            name='SMSCase',
            bases=[Name(id='MockSMS', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Main test class to use when testing SMS integrations. Contains helpers and tools related\n    to notification sent by SMS. ', kind=None),
                ),
                FunctionDef(
                    name='_find_sms_sent',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='number', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Name(id='partner', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='phone_get_sanitized_number',
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
                        Assign(
                            targets=[Name(id='sent_sms', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='sms', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='sms', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_sms',
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='sms', ctx=Load()),
                                                            slice=Constant(value='number', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='number', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sent_sms', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='sent sms not found for %s (number: %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='partner', ctx=Load()),
                                                        Name(id='number', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                            value=Name(id='sent_sms', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_sms_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='number', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Name(id='partner', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='phone_get_sanitized_number',
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
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_new_sms',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='number', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='number', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='status', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='status', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sms', ctx=Store())],
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
                                                slice=Constant(value='sms.sms', kind=None),
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
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sms', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='sms.sms not found for %s (number: %s / status %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='partner', ctx=Load()),
                                                        Name(id='number', ctx=Load()),
                                                        Name(id='status', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='sms', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='NotImplementedError', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='sms', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertNoSMS',
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
                            value=Constant(value=' Check no sms went through gateway during mock. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_new_sms',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
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
                    name='assertSMSIapSent',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='numbers', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check sent SMS. Order is not checked. Each number should have received\n        the same content. Useful to check batch sending.\n\n        :param numbers: list of numbers;\n        :param content: content to check for each number;\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='number', ctx=Store()),
                            iter=Name(id='numbers', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='sent_sms', ctx=Store())],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='sms', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='sms', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_sms',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='sms', ctx=Load()),
                                                                    slice=Constant(value='number', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='number', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
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
                                        args=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[Name(id='sent_sms', ctx=Load())],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Constant(value='Number %s not found in %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='number', ctx=Load()),
                                                        Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                ListComp(
                                                                    elt=Subscript(
                                                                        value=Name(id='s', ctx=Load()),
                                                                        slice=Constant(value='number', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='s', ctx=Store()),
                                                                            iter=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='_sms',
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
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='content', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='content', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='sent_sms', ctx=Load()),
                                                        slice=Constant(value='body', kind=None),
                                                        ctx=Load(),
                                                    ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertSMSSent',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='numbers', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Deprecated. Remove in 14.4 ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSIapSent',
                                    ctx=Load(),
                                ),
                                args=[Name(id='numbers', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='content',
                                        value=Name(id='content', ctx=Load()),
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
                    name='assertSMS',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='failure_type', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='fields_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Find a ``sms.sms`` record, based on given partner, number and status.\n\n        :param partner: optional partner, used to find a ``sms.sms`` and a number\n          if not given;\n        :param number: optional number, used to find a ``sms.sms``, notably if\n          partner is not given;\n        :param failure_type: check failure type if SMS is not sent or outgoing;\n        :param content: if given, should be contained in sms body;\n        :param fields_values: optional values allowing to check directly some\n          values on ``sms.sms`` record;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sms_sms', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_sms_sms',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='partner', ctx=Load()),
                                    Name(id='number', ctx=Load()),
                                    Name(id='status', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='failure_type', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='sms_sms', ctx=Load()),
                                                attr='failure_type',
                                                ctx=Load(),
                                            ),
                                            Name(id='failure_type', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='content', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='content', ctx=Load()),
                                            Attribute(
                                                value=Name(id='sms_sms', ctx=Load()),
                                                attr='body',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='fname', ctx=Store()),
                                    Name(id='fvalue', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='fields_values', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                    attr='items',
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='sms_sms', ctx=Load()),
                                                slice=Name(id='fname', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Name(id='fvalue', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='SMS: expected %s for %s, got %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='fvalue', ctx=Load()),
                                                        Name(id='fname', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='sms_sms', ctx=Load()),
                                                            slice=Name(id='fname', ctx=Load()),
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
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='status', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sent', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertSMSIapSent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='sms_sms', ctx=Load()),
                                                        attr='number',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='content',
                                                value=Name(id='content', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertSMSCanceled',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                            arg(arg='failure_type', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='fields_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check canceled SMS. Search is done for a pair partner / number where\n        partner can be an empty recordset. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMS',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='partner', ctx=Load()),
                                    Name(id='number', ctx=Load()),
                                    Constant(value='canceled', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='failure_type',
                                        value=Name(id='failure_type', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='content',
                                        value=Name(id='content', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields_values',
                                        value=Name(id='fields_values', ctx=Load()),
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
                    name='assertSMSFailed',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                            arg(arg='failure_type', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='fields_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check failed SMS. Search is done for a pair partner / number where\n        partner can be an empty recordset. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMS',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='partner', ctx=Load()),
                                    Name(id='number', ctx=Load()),
                                    Constant(value='error', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='failure_type',
                                        value=Name(id='failure_type', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='content',
                                        value=Name(id='content', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields_values',
                                        value=Name(id='fields_values', ctx=Load()),
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
                    name='assertSMSOutgoing',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='fields_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check outgoing SMS. Search is done for a pair partner / number where\n        partner can be an empty recordset. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMS',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='partner', ctx=Load()),
                                    Name(id='number', ctx=Load()),
                                    Constant(value='outgoing', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='content',
                                        value=Name(id='content', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields_values',
                                        value=Name(id='fields_values', ctx=Load()),
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
                    name='assertNoSMSNotification',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='messages', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='base_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='sms', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='messages', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='base_domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='mail_message_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='messages', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
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
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.notification', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='base_domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.notification', kind=None),
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sms',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                    name='assertSMSNotification',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='messages', annotation=None, type_comment=None),
                            arg(arg='check_sms', annotation=None, type_comment=None),
                            arg(arg='sent_unlink', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check content of notifications.\n\n          :param recipients_info: list[{\n            'partner': res.partner record (may be empty),\n            'number': number used for notification (may be empty, computed based on partner),\n            'state': ready / sent / exception / canceled (sent by default),\n            'failure_type': optional: sms_number_missing / sms_number_format / sms_credit / sms_server\n            }, { ... }]\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='concat',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Call(
                                            func=Name(id='list', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='p', ctx=Load()),
                                                        slice=Constant(value='partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='p', ctx=Store()),
                                                            iter=Name(id='recipients_info', ctx=Load()),
                                                            ifs=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='p', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='partner', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='numbers', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='p', ctx=Load()),
                                    slice=Constant(value='number', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='p', ctx=Store()),
                                        iter=Name(id='recipients_info', ctx=Load()),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='number', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
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
                                        operand=Name(id='partners', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='numbers', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='numbers', ctx=Store())],
                                    value=List(
                                        elts=[Constant(value=False, kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='base_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='res_partner_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='partners', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='&', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='res_partner_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sms_number', kind=None),
                                            Constant(value='in', kind=None),
                                            Name(id='numbers', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='sms', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='messages', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='base_domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='mail_message_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='messages', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='notifications', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.notification', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='base_domain', ctx=Load())],
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
                                        func=Attribute(
                                            value=Name(id='notifications', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res_partner_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='partners', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='recipient_info', ctx=Store()),
                            iter=Name(id='recipients_info', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner', kind=None),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='number', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='state', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='state', kind=None),
                                            Constant(value='sent', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='number', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Name(id='partner', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='number', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='phone_get_sanitized_number',
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
                                Assign(
                                    targets=[Name(id='notif', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='notifications', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='n', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='n', ctx=Load()),
                                                                attr='res_partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='partner', ctx=Load())],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='n', ctx=Load()),
                                                                attr='sms_number',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='number', ctx=Load())],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='n', ctx=Load()),
                                                                attr='notification_status',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='state', ctx=Load())],
                                                        ),
                                                    ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='notif', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='SMS: not found notification for %s (number: %s, state: %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='partner', ctx=Load()),
                                                        Name(id='number', ctx=Load()),
                                                        Name(id='state', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='state', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sent', kind=None),
                                                    Constant(value='ready', kind=None),
                                                    Constant(value='canceled', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='notif', ctx=Load()),
                                                        attr='failure_type',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='recipient_info', ctx=Load()),
                                                        slice=Constant(value='failure_type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='check_sms', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sent', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='sent_unlink', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertSMSIapSent',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='number', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertSMS',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partner', ctx=Load()),
                                                                    Name(id='number', ctx=Load()),
                                                                    Constant(value='sent', kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='state', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ready', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertSMS',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partner', ctx=Load()),
                                                                    Name(id='number', ctx=Load()),
                                                                    Constant(value='outgoing', kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='state', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='exception', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='assertSMS',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='partner', ctx=Load()),
                                                                            Name(id='number', ctx=Load()),
                                                                            Constant(value='error', kind=None),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='failure_type',
                                                                                value=Subscript(
                                                                                    value=Name(id='recipient_info', ctx=Load()),
                                                                                    slice=Constant(value='failure_type', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='content',
                                                                                value=Name(id='content', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='state', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='canceled', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='assertSMS',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Name(id='partner', ctx=Load()),
                                                                                    Name(id='number', ctx=Load()),
                                                                                    Constant(value='canceled', kind=None),
                                                                                ],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='failure_type',
                                                                                        value=Subscript(
                                                                                            value=Name(id='recipient_info', ctx=Load()),
                                                                                            slice=Constant(value='failure_type', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='content',
                                                                                        value=Name(id='content', ctx=Load()),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='NotImplementedError', ctx=Load()),
                                                                                args=[Constant(value='Not implemented', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='messages', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='message', ctx=Store()),
                                    iter=Name(id='messages', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='content', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tools', ctx=Load()),
                                                                    attr='html2plaintext',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='message', ctx=Load()),
                                                                        attr='body',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='rstrip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='\n', kind=None)],
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
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertSMSLogged',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='records', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_ids',
                                            ctx=Load(),
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
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
                                            Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='subtype_id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail.mt_note', kind=None)],
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='message_type',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sms', kind=None),
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
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='html2plaintext',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='message', ctx=Load()),
                                                                attr='body',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='\n', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='body', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='SMSCommon',
            bases=[
                Name(id='MailCommon', ctx=Load()),
                Name(id='MockSMS', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SMSCommon', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='user_employee',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='login', kind=None)],
                                        values=[Constant(value='employee', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='user_employee',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='country_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.be', kind=None)],
                                                    keywords=[],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='random_numbers_str',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='+32456998877, 0456665544', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='random_numbers',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='random_numbers_str',
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=', ', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='random_numbers_san',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='phone_validation', ctx=Load()),
                                        attr='phone_format',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='number', ctx=Load()),
                                        Constant(value='BE', kind=None),
                                        Constant(value='32', kind=None),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='force_format',
                                            value=Constant(value='E164', kind=None),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='number', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='random_numbers',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_numbers',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Constant(value='+32456010203', kind=None),
                                    Constant(value='0456 04 05 06', kind=None),
                                    Constant(value='0032456070809', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_numbers_san',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='phone_validation', ctx=Load()),
                                        attr='phone_format',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='number', ctx=Load()),
                                        Constant(value='BE', kind=None),
                                        Constant(value='32', kind=None),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='force_format',
                                            value=Constant(value='E164', kind=None),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='number', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='test_numbers',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mass_numbers',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=BinOp(
                                    left=Constant(value='04561%s2%s3%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Name(id='x', ctx=Load()),
                                            Name(id='x', ctx=Load()),
                                            Name(id='x', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Constant(value=0, kind=None),
                                                Constant(value=10, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mass_numbers_san',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='phone_validation', ctx=Load()),
                                        attr='phone_format',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='number', ctx=Load()),
                                        Constant(value='BE', kind=None),
                                        Constant(value='32', kind=None),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='force_format',
                                            value=Constant(value='E164', kind=None),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='number', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='mass_numbers',
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
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_sms_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sms.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='body', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Template', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='cls', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='model', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            IfExp(
                                                test=Name(id='body', ctx=Load()),
                                                body=Name(id='body', ctx=Load()),
                                                orelse=Constant(value='Dear {{ object.display_name }} this is an SMS.', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
