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
                    name='action_mass_mailing_track_speakers',
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
                            targets=[Name(id='mass_mailing_action', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Mass Mail Attendees', kind=None),
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
                                                            args=[Constant(value='website_event_track.model_event_track', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='default_mailing_domain',
                                                    value=Call(
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
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='stage_id.is_cancel', kind=None),
                                                                            Constant(value='!=', kind=None),
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
