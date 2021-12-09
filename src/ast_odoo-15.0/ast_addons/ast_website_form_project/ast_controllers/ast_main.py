Module(
    body=[
        ImportFrom(
            module='odoo.addons.website.controllers',
            names=[alias(name='form', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteForm',
            bases=[
                Attribute(
                    value=Name(id='form', ctx=Load()),
                    attr='WebsiteForm',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='insert_record',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='request', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='custom', annotation=None, type_comment=None),
                            arg(arg='meta', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='model',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='project.task', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='visitor_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.visitor', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_visitor_from_request',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='visitor_partner', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='visitor_sudo', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='visitor_partner', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='partner_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='visitor_partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='insert_record',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='request', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                    Name(id='custom', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='meta',
                                        value=Name(id='meta', ctx=Load()),
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
