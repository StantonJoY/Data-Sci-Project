Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=43,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=55,
            end_col_offset=26,
            name='TimesheetAttendance',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=26,
                    end_lineno=7,
                    end_col_offset=38,
                    value=Name(lineno=7, col_offset=26, end_lineno=7, end_col_offset=32, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=44,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=44, value='hr.timesheet.attendance.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=17,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, id='_auto', ctx=Store())],
                    value=Constant(lineno=9, col_offset=12, end_lineno=9, end_col_offset=17, value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=48,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=10, col_offset=19, end_lineno=10, end_col_offset=48, value='Timesheet Attendance Report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=42,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=11, id='user_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=14,
                        end_lineno=12,
                        end_col_offset=42,
                        func=Attribute(
                            lineno=12,
                            col_offset=14,
                            end_lineno=12,
                            end_col_offset=29,
                            value=Name(lineno=12, col_offset=14, end_lineno=12, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=30, end_lineno=12, end_col_offset=41, value='res.users', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=24,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=8, id='date', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=11,
                        end_lineno=13,
                        end_col_offset=24,
                        func=Attribute(
                            lineno=13,
                            col_offset=11,
                            end_lineno=13,
                            end_col_offset=22,
                            value=Name(lineno=13, col_offset=11, end_lineno=13, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=36,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=19, id='total_timesheet', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=22,
                        end_lineno=14,
                        end_col_offset=36,
                        func=Attribute(
                            lineno=14,
                            col_offset=22,
                            end_lineno=14,
                            end_col_offset=34,
                            value=Name(lineno=14, col_offset=22, end_lineno=14, end_col_offset=28, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=37,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=20, id='total_attendance', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=23,
                        end_lineno=15,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=15,
                            col_offset=23,
                            end_lineno=15,
                            end_col_offset=35,
                            value=Name(lineno=15, col_offset=23, end_lineno=15, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=37,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=20, id='total_difference', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=23,
                        end_lineno=16,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=16,
                            col_offset=23,
                            end_lineno=16,
                            end_col_offset=35,
                            value=Name(lineno=16, col_offset=23, end_lineno=16, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=80,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=14, id='company_id', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=17,
                        end_lineno=17,
                        end_col_offset=80,
                        func=Attribute(
                            lineno=17,
                            col_offset=17,
                            end_lineno=17,
                            end_col_offset=32,
                            value=Name(lineno=17, col_offset=17, end_lineno=17, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=33, end_lineno=17, end_col_offset=46, value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=48,
                                end_lineno=17,
                                end_col_offset=64,
                                arg='string',
                                value=Constant(lineno=17, col_offset=55, end_lineno=17, end_col_offset=64, value='Company', kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=66,
                                end_lineno=17,
                                end_col_offset=79,
                                arg='readonly',
                                value=Constant(lineno=17, col_offset=75, end_lineno=17, end_col_offset=79, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=19,
                    col_offset=4,
                    end_lineno=55,
                    end_col_offset=26,
                    name='init',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=19, col_offset=13, end_lineno=19, end_col_offset=17, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=59,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=59,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=33,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=13, id='tools', ctx=Load()),
                                    attr='drop_view_if_exists',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=20,
                                        col_offset=34,
                                        end_lineno=20,
                                        end_col_offset=45,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=34,
                                            end_lineno=20,
                                            end_col_offset=42,
                                            value=Name(lineno=20, col_offset=34, end_lineno=20, end_col_offset=38, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=20,
                                        col_offset=47,
                                        end_lineno=20,
                                        end_col_offset=58,
                                        value=Name(lineno=20, col_offset=47, end_lineno=20, end_col_offset=51, id='self', ctx=Load()),
                                        attr='_table',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=21,
                            col_offset=8,
                            end_lineno=55,
                            end_col_offset=26,
                            value=Call(
                                lineno=21,
                                col_offset=8,
                                end_lineno=55,
                                end_col_offset=26,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=8,
                                    end_lineno=21,
                                    end_col_offset=24,
                                    value=Attribute(
                                        lineno=21,
                                        col_offset=8,
                                        end_lineno=21,
                                        end_col_offset=16,
                                        value=Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=12, id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=21,
                                        col_offset=25,
                                        end_lineno=55,
                                        end_col_offset=25,
                                        left=Constant(lineno=21, col_offset=25, end_lineno=55, end_col_offset=11, value='CREATE OR REPLACE VIEW %s AS (\n            SELECT\n                max(id) AS id,\n                t.user_id,\n                t.date,\n                t.company_id,\n                coalesce(sum(t.attendance), 0) AS total_attendance,\n                coalesce(sum(t.timesheet), 0) AS total_timesheet,\n                coalesce(sum(t.attendance), 0) - coalesce(sum(t.timesheet), 0) as total_difference\n            FROM (\n                SELECT\n                    -hr_attendance.id AS id,\n                    resource_resource.user_id AS user_id,\n                    hr_attendance.worked_hours AS attendance,\n                    NULL AS timesheet,\n                    hr_attendance.check_in::date AS date,\n                    resource_resource.company_id as company_id\n                FROM hr_attendance\n                LEFT JOIN hr_employee ON hr_employee.id = hr_attendance.employee_id\n                LEFT JOIN resource_resource on resource_resource.id = hr_employee.resource_id\n            UNION ALL\n                SELECT\n                    ts.id AS id,\n                    ts.user_id AS user_id,\n                    NULL AS attendance,\n                    ts.unit_amount AS timesheet,\n                    ts.date AS date,\n                    NULL AS company_id\n                FROM account_analytic_line AS ts\n                WHERE ts.project_id IS NOT NULL\n            ) AS t\n            GROUP BY t.user_id, t.date, t.company_id\n            ORDER BY t.date\n        )\n        ', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            lineno=55,
                                            col_offset=14,
                                            end_lineno=55,
                                            end_col_offset=25,
                                            value=Name(lineno=55, col_offset=14, end_lineno=55, end_col_offset=18, id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)