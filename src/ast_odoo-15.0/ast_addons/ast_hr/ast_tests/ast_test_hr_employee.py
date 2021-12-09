Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hr.tests.common',
            names=[alias(name='TestHrCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestHrEmployee',
            bases=[Name(id='TestHrCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_employee_resource',
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
                            targets=[Name(id='_tz', ctx=Store())],
                            value=Constant(value='Pacific/Apia', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_users_hr_officer',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='_tz', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_users_hr_officer',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[Name(id='Employee', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Raoul Grosbedon', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='work_email',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='raoul@example.com', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='employee', ctx=Load()),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                    Name(id='_tz', ctx=Load()),
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
                    name='test_employee_from_user',
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
                            targets=[Name(id='_tz', ctx=Store())],
                            value=Constant(value='Pacific/Apia', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='_tz2', ctx=Store())],
                            value=Constant(value='America/Tijuana', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_users_hr_officer',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='_tz', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_users_hr_officer',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='_tz2', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_users_hr_officer',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[Name(id='Employee', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Raoul Grosbedon', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='work_email',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='raoul@example.com', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='user_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='res_users_hr_officer',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='employee', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Raoul Grosbedon', kind=None),
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
                                        value=Name(id='employee', ctx=Load()),
                                        attr='work_email',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='res_users_hr_officer',
                                            ctx=Load(),
                                        ),
                                        attr='email',
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
                                        value=Name(id='employee', ctx=Load()),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='res_users_hr_officer',
                                            ctx=Load(),
                                        ),
                                        attr='tz',
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
                    name='test_employee_from_user_tz_no_reset',
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
                            targets=[Name(id='_tz', ctx=Store())],
                            value=Constant(value='Pacific/Apia', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_users_hr_officer',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_users_hr_officer',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[Name(id='Employee', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Raoul Grosbedon', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='work_email',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='raoul@example.com', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='_tz', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
                                    attr='user_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='res_users_hr_officer',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='employee_form', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='employee', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Raoul Grosbedon', kind=None),
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
                                        value=Name(id='employee', ctx=Load()),
                                        attr='work_email',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='res_users_hr_officer',
                                            ctx=Load(),
                                        ),
                                        attr='email',
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
                                        value=Name(id='employee', ctx=Load()),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                    Name(id='_tz', ctx=Load()),
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
