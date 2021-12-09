Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Event',
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
                    value=Constant(value='event.event', kind=None),
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Constant(value='Mass Mail Attendees', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='mailing.mailing', kind=None),
                                    Constant(value='form', kind=None),
                                    Constant(value='current', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='default_mailing_model_id', kind=None),
                                            Constant(value='default_mailing_domain', kind=None),
                                        ],
                                        values=[
                                            Attribute(
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
                                                    args=[Constant(value='event.model_event_registration', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='repr', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='event_id', kind=None),
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
                                        ],
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
                    name='action_invite_contacts',
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Constant(value='Mass Mail Invitation', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='mailing.mailing', kind=None),
                                    Constant(value='form', kind=None),
                                    Constant(value='current', kind=None),
                                    Dict(
                                        keys=[Constant(value='default_mailing_model_id', kind=None)],
                                        values=[
                                            Attribute(
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
                                        ],
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
