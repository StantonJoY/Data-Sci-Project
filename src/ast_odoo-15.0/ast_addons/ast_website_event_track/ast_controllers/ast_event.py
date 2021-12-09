Module(
    body=[
        ImportFrom(
            module='odoo.addons.website_event.controllers.main',
            names=[alias(name='WebsiteEventController', asname=None)],
            level=0,
        ),
        ClassDef(
            name='EventOnlineController',
            bases=[Name(id='WebsiteEventController', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_get_registration_confirm_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='attendees_sudo', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='EventOnlineController', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_registration_confirm_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='attendees_sudo', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='hide_sponsors', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
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
