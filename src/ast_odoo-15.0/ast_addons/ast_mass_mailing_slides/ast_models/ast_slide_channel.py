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
            name='Course',
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
                    value=Constant(value='slide.channel', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_mass_mailing_attendees',
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
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Name(id='repr', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slide_channel_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mass_mailing_action', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Mass Mail Course Members', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='ir.actions.act_window', kind=None),
                                    ),
                                    keyword(
                                        arg='res_model',
                                        value=Constant(value='mailing.mailing', kind=None),
                                    ),
                                    keyword(
                                        arg='view_mode',
                                        value=Constant(value='form', kind=None),
                                    ),
                                    keyword(
                                        arg='target',
                                        value=Constant(value='current', kind=None),
                                    ),
                                    keyword(
                                        arg='context',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='default_mailing_model_id',
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='base.model_res_partner', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_mailing_domain',
                                                    value=Name(id='domain', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='mass_mailing_action', ctx=Load()),
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
