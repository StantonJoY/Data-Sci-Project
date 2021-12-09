Module(
    body=[
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='html', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests',
            names=[alias(name='common', asname='mail_test')],
            level=0,
        ),
        ClassDef(
            name='TestDigest',
            bases=[
                Attribute(
                    value=Name(id='mail_test', ctx=Load()),
                    attr='MailCommon',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_digest_numbers',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_setup_messages',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='digest', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='digest.digest', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='kpi_mail_message_total', kind=None),
                                        ],
                                        values=[
                                            Constant(value='My Digest', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='digest_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='digest', ctx=Load()),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_employee',
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
                                    value=Name(id='digest_user', ctx=Load()),
                                    attr='action_subscribe',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='digest_user', ctx=Load()),
                                        attr='is_subscribed',
                                        ctx=Load(),
                                    ),
                                    Constant(value='check the user was subscribed as action_subscribe will silently ignore subs of non-employees', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mock_mail_gateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='digest', ctx=Load()),
                                            attr='action_send',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_mails',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='a mail has been created for the digest', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_mails',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='body', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='kpi_message_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='html', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='body', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//div[@data-field="kpi_mail_message_total"]//*[hasclass("kpi_value")]/text()', kind=None)],
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
                                    ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='t', ctx=Store()),
                                                iter=Name(id='kpi_message_values', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='3', kind=None),
                                            Constant(value='8', kind=None),
                                            Constant(value='15', kind=None),
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
                    name='_setup_messages',
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
                            value=Constant(value=' Remove all existing messages, then create a bunch of them on random\n        partners with the correct types in correct time-bucket:\n\n        - 3 in the previous 24h\n        - 5 more in the 6 days before that for a total of 8 in the previous week\n        - 7 more in the 20 days before *that* (because digest doc lies and is\n          based around weeks and months not days), for a total of 15 in the\n          previous month\n        ', kind=None),
                        ),
                        Expr(
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
                                                slice=Constant(value='mail.message', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='now', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='private', kind=None),
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
                            targets=[Name(id='counter', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='count',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='count', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='low', ctx=Store()),
                                            Name(id='high', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value=0, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=24, kind=None),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value=1, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=24, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=5, kind=None),
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value=1, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=24, kind=None),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value=7, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=24, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=7, kind=None),
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value=7, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=24, kind=None),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value=27, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=24, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='_', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Name(id='count', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='create_date', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='now', ctx=Load()),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='hours',
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='randint',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='low', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    BinOp(
                                                                        left=Name(id='high', ctx=Load()),
                                                                        op=Sub(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='random', ctx=Load()),
                                                            attr='choice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='partners', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=JoinedStr(
                                                            values=[
                                                                Constant(value='Awesome Partner! (', kind=None),
                                                                FormattedValue(
                                                                    value=Call(
                                                                        func=Name(id='next', ctx=Load()),
                                                                        args=[Name(id='counter', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value=')', kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='message_type',
                                                        value=Constant(value='comment', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='subtype_xmlid',
                                                        value=Constant(value='mail.mt_comment', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='create_date',
                                                        value=Name(id='create_date', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
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
    ],
    type_ignores=[],
)
