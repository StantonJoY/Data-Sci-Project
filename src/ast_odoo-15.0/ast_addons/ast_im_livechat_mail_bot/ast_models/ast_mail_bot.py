Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MailBot',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.bot', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_answer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='command', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='odoobot_state', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='odoobot_state',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_bot_in_private_channel',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='odoobot_state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='onboarding_attachement', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='attachment_ids', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='odoobot_failed',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='odoobot_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='onboarding_canned', kind=None),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='That\'s me! 🎉<br/>Try typing <span class="o_odoobot_command">:</span> to use canned responses.', kind=None)],
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
                                                        left=Name(id='odoobot_state', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='onboarding_canned', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='canned_response_ids', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='odoobot_failed',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='odoobot_state',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='idle', kind=None),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="Good, you can customize canned responses in the live chat application.<br/><br/><b>It's the end of this overview</b>, enjoy discovering Odoo!", kind=None)],
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
                                                                left=Name(id='odoobot_state', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='onboarding_canned', kind=None)],
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_is_help_requested',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='body', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='user',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='odoobot_failed',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Return(
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Not sure what you are doing. Please, type <span class="o_odoobot_command">:</span> and wait for the propositions. Select one of them and press enter.', kind=None)],
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
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailBot', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_answer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='body', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                    Name(id='command', ctx=Load()),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
