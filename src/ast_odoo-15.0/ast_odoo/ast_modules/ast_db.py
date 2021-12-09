Module(
    body=[
        Import(
            names=[alias(name='odoo.modules', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='is_initialized',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Check if a database has been initialized for the ORM.\n\n    The database can be initialized with the 'initialize' function below.\n\n    ", kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='table_exists',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Constant(value='ir_module_module', kind=None),
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
            name='initialize',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Initialize a database with for the ORM.\n\n    This executes base/data/base_data.sql, creates the ir_module_categories\n    (taken from each module descriptor file), and creates the ir_module_module\n    and ir_model_data entries.\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='f', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='modules',
                                ctx=Load(),
                            ),
                            attr='get_module_resource',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='base', kind=None),
                            Constant(value='data', kind=None),
                            Constant(value='base_data.sql', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='f', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='m', ctx=Store())],
                            value=Constant(value="File not found: 'base.sql' (provided by module 'base').", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='critical',
                                    ctx=Load(),
                                ),
                                args=[Name(id='m', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='IOError', ctx=Load()),
                                args=[Name(id='m', ctx=Load())],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='misc',
                                        ctx=Load(),
                                    ),
                                    attr='file_open',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[],
                            ),
                            optional_vars=Name(id='base_sql_file', ctx=Store()),
                        ),
                    ],
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='base_sql_file', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
                For(
                    target=Name(id='i', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='modules',
                                ctx=Load(),
                            ),
                            attr='get_modules',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mod_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='get_module_path',
                                    ctx=Load(),
                                ),
                                args=[Name(id='i', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='mod_path', ctx=Load()),
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='load_information_from_description_file',
                                    ctx=Load(),
                                ),
                                args=[Name(id='i', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='info', ctx=Load()),
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='categories', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='info', ctx=Load()),
                                        slice=Constant(value='category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='category_id', ctx=Store())],
                            value=Call(
                                func=Name(id='create_categories', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='categories', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='info', ctx=Load()),
                                slice=Constant(value='installable', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='state', ctx=Store())],
                                    value=Constant(value='uninstalled', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='state', ctx=Store())],
                                    value=Constant(value='uninstallable', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='INSERT INTO ir_module_module                 (author, website, name, shortdesc, description,                     category_id, auto_install, state, web, license, application, icon, sequence, summary)                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id', kind=None),
                                    Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='author', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='i', ctx=Load()),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='description', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='category_id', ctx=Load()),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='info', ctx=Load()),
                                                    slice=Constant(value='auto_install', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            Name(id='state', ctx=Load()),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='web', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='license', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='application', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='icon', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='sequence', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='summary', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='fetchone',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='INSERT INTO ir_model_data             (name,model,module, res_id, noupdate) VALUES (%s,%s,%s,%s,%s)', kind=None),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='module_', kind=None),
                                                op=Add(),
                                                right=Name(id='i', ctx=Load()),
                                            ),
                                            Constant(value='ir.module.module', kind=None),
                                            Constant(value='base', kind=None),
                                            Name(id='id', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dependencies', ctx=Store())],
                            value=Subscript(
                                value=Name(id='info', ctx=Load()),
                                slice=Constant(value='depends', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='d', ctx=Store()),
                            iter=Name(id='dependencies', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='INSERT INTO ir_module_module_dependency (module_id, name, auto_install_required) VALUES (%s, %s, %s)', kind=None),
                                            Tuple(
                                                elts=[
                                                    Name(id='id', ctx=Load()),
                                                    Name(id='d', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='d', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Subscript(
                                                                        value=Name(id='info', ctx=Load()),
                                                                        slice=Constant(value='auto_install', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(elts=[], ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                While(
                    test=Constant(value=True, kind=None),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="\n        SELECT m.name FROM ir_module_module m\n        WHERE m.auto_install\n        AND state != 'to install'\n        AND NOT EXISTS (\n            SELECT 1 FROM ir_module_module_dependency d\n            JOIN ir_module_module mdep ON (d.name = mdep.name)\n            WHERE d.module_id = m.id\n              AND d.auto_install_required\n              AND mdep.state != 'to install'\n        )", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='to_auto_install', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='x', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='cr', ctx=Load()),
                                                attr='fetchall',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="\n        SELECT d.name FROM ir_module_module_dependency d\n        JOIN ir_module_module m ON (d.module_id = m.id)\n        JOIN ir_module_module mdep ON (d.name = mdep.name)\n        WHERE (m.state = 'to install' OR m.name = any(%s))\n            -- don't re-mark marked modules\n        AND NOT (mdep.state = 'to install' OR mdep.name = any(%s))\n        ", kind=None),
                                    List(
                                        elts=[
                                            Name(id='to_auto_install', ctx=Load()),
                                            Name(id='to_auto_install', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='to_auto_install', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='x', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='cr', ctx=Load()),
                                                        attr='fetchall',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
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
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='to_auto_install', ctx=Load()),
                            ),
                            body=[Break()],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="UPDATE ir_module_module SET state='to install' WHERE name in %s", kind=None),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='to_auto_install', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='create_categories',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='categories', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Create the ir_module_category entries for some categories.\n\n    categories is a list of strings forming a single category with its\n    parent categories, like ['Grand Parent', 'Parent', 'Child'].\n\n    Return the database id of the (last) category.\n\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='p_id', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='category', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                While(
                    test=Name(id='categories', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='categories', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xml_id', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='module_category_', kind=None),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Constant(value='_', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Call(
                                                                func=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='x', ctx=Store()),
                                                                    iter=Name(id='category', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='replace',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='&', kind=None),
                                                Constant(value='and', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='replace',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value=' ', kind=None),
                                        Constant(value='_', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT res_id FROM ir_model_data WHERE name=%s AND module=%s AND model=%s', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='xml_id', ctx=Load()),
                                            Constant(value='base', kind=None),
                                            Constant(value='ir.module.category', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='c_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='c_id', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='INSERT INTO ir_module_category                     (name, parent_id)                     VALUES (%s, %s) RETURNING id', kind=None),
                                            Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='categories', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='p_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='c_id', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cr', ctx=Load()),
                                                attr='fetchone',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='INSERT INTO ir_model_data (module, name, res_id, model, noupdate)                        VALUES (%s, %s, %s, %s, %s)', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='base', kind=None),
                                                    Name(id='xml_id', ctx=Load()),
                                                    Name(id='c_id', ctx=Load()),
                                                    Constant(value='ir.module.category', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='c_id', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='c_id', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='p_id', ctx=Store())],
                            value=Name(id='c_id', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='categories', ctx=Store())],
                            value=Subscript(
                                value=Name(id='categories', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='p_id', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='has_unaccent',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Test if the database has an unaccent function.\n\n    The unaccent is supposed to be provided by the PostgreSQL unaccent contrib\n    module but any similar function will be picked by OpenERP.\n\n    ', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[Constant(value="SELECT proname FROM pg_proc WHERE proname='unaccent'", kind=None)],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='fetchall',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[Constant(value=0, kind=None)],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='has_trigram',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Test if the database has the a word_similarity function.\n\n    The word_similarity is supposed to be provided by the PostgreSQL built-in\n    pg_trgm module but any similar function will be picked by Odoo.\n\n    ', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[Constant(value="SELECT proname FROM pg_proc WHERE proname='word_similarity'", kind=None)],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='fetchall',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[Constant(value=0, kind=None)],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
