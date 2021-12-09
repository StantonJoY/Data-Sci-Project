Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mass_mailing.tests.common',
            names=[alias(name='MassMailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='users', asname=None),
                alias(name='Form', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMailingScheduleDateWizard',
            bases=[Name(id='MassMailCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_mailing_schedule_date',
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
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='mailing_model_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='mailing', kind=None),
                                            Constant(value='some subject', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='res.partner', kind=None)],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mailing.mailing.schedule.date', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_mass_mailing_id',
                                                value=Attribute(
                                                    value=Name(id='mailing', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='wizard_form', ctx=Load()),
                                    attr='schedule_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2021, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=30, kind=None),
                                    Constant(value=9, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='wizard_form', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='wizard', ctx=Load()),
                                    attr='action_schedule_date',
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
                                    Attribute(
                                        value=Name(id='mailing', ctx=Load()),
                                        attr='schedule_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='mailing', ctx=Load()),
                                        attr='schedule_type',
                                        ctx=Load(),
                                    ),
                                    Constant(value='scheduled', kind=None),
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
                                        value=Name(id='mailing', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='in_queue', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.mail.models.mail_mail', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
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
