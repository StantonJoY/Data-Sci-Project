Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.loading',
            names=[alias(name='force_demo', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_module',
            names=[alias(name='assert_log_admin_access', asname=None)],
            level=0,
        ),
        ClassDef(
            name='IrDemo',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.demo', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Demo', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='install_demo',
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
                                func=Name(id='force_demo', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='url', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_url', kind=None),
                                    Constant(value='self', kind=None),
                                    Constant(value='/web', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='assert_log_admin_access', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
