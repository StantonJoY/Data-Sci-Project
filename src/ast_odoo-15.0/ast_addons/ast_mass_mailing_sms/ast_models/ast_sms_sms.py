Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SmsSms',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='sms.sms', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mailing_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mailing.mailing', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Mass Mailing', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mailing_trace_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mailing.trace', kind=None),
                            Constant(value='sms_sms_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Statistics', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_body_short_links',
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
                            value=Constant(value=' Override to tweak shortened URLs by adding statistics ids, allowing to\n        find customer back once clicked. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sms', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='sms', ctx=Load()),
                                                    attr='mailing_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='sms', ctx=Load()),
                                                    attr='body',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='sms', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='sms', ctx=Load()),
                                                attr='body',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='sms', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='url', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='findall',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='TEXT_URL_REGEX',
                                                ctx=Load(),
                                            ),
                                            Name(id='body', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='url', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='sms', ctx=Load()),
                                                                attr='get_base_url',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='/r/', kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='body', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='body', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='url', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='url', ctx=Load()),
                                                                op=Add(),
                                                                right=BinOp(
                                                                    left=Constant(value='/s/%s', kind=None),
                                                                    op=Mod(),
                                                                    right=Attribute(
                                                                        value=Name(id='sms', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
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
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='sms', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='body', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                    name='_postprocess_iap_sent_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='iap_results', annotation=None, type_comment=None),
                            arg(arg='failure_reason', annotation=None, type_comment=None),
                            arg(arg='unlink_failed', annotation=None, type_comment=None),
                            arg(arg='unlink_sent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='all_sms_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='item', ctx=Load()),
                                    slice=Constant(value='res_id', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='item', ctx=Store()),
                                        iter=Name(id='iap_results', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='sms', ctx=Load()),
                                            attr='mailing_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='sms', ctx=Store()),
                                                iter=Call(
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
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='all_sms_ids', ctx=Load())],
                                                    keywords=[],
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
                                For(
                                    target=Name(id='state', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='IAP_TO_SMS_STATE',
                                                ctx=Load(),
                                            ),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sms_ids', ctx=Store())],
                                            value=ListComp(
                                                elt=Subscript(
                                                    value=Name(id='item', ctx=Load()),
                                                    slice=Constant(value='res_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='item', ctx=Store()),
                                                        iter=Name(id='iap_results', ctx=Load()),
                                                        ifs=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    slice=Constant(value='state', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='state', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='traces', ctx=Store())],
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
                                                                slice=Constant(value='mailing.trace', kind=None),
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
                                                                    Constant(value='sms_sms_id_int', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='sms_ids', ctx=Load()),
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
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='traces', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='state', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='success', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='traces', ctx=Load()),
                                                            attr='set_sent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='traces', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='traces', ctx=Load()),
                                                                    attr='set_failed',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='failure_type',
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='IAP_TO_SMS_STATE',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Name(id='state', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SmsSms', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_postprocess_iap_sent_sms',
                                    ctx=Load(),
                                ),
                                args=[Name(id='iap_results', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='failure_reason',
                                        value=Name(id='failure_reason', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='unlink_failed',
                                        value=Name(id='unlink_failed', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='unlink_sent',
                                        value=Name(id='unlink_sent', ctx=Load()),
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
